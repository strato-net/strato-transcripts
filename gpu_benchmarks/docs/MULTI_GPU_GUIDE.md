# Multi-GPU Benchmarking Guide

This guide explains how to use the GPU benchmarking suite to test and compare results across multiple GPUs.

## Overview

The benchmarking suite has been enhanced to support testing multiple GPUs with clear differentiation and comparison capabilities.

### Key Features:
- **GPU-specific result files** with GPU ID and name in filename
- **Structured JSON output** with complete GPU metadata
- **Comparison tools** to analyze results across multiple GPUs
- **Batch testing** to run tests on all available GPUs
- **Automated reporting** with rankings and summaries

---

## File Naming Convention

All result files now follow a standardized naming convention that includes GPU identification:

### Benchmark Results:
```
benchmark_GPU{id}_{gpu_name}_{timestamp}.json
```
Example: `benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_195914.json`

### Stress Test Results:
```
stress_test_GPU{id}_{gpu_name}_{timestamp}.json
```
Example: `stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_200151.json`

### Comparison Reports:
```
comparison_report_{timestamp}.txt
```
Example: `comparison_report_20260122_200500.txt`

---

## JSON Structure

All result files contain:

### GPU Information:
```json
"gpu_info": {
  "id": 0,
  "name": "NVIDIA GeForce RTX 3090",
  "total_memory_gb": 23.55,
  "cuda_capability": "8.6",
  "multiprocessor_count": 82,
  "max_threads_per_multiprocessor": 1536,
  "warp_size": 32
}
```

### Test Metadata:
```json
"test_metadata": {
  "timestamp": "2026-01-22T19:59:14.181995",
  "date": "2026-01-22",
  "time": "19:59:14",
  "pytorch_version": "2.9.1+cu130",
  "cuda_version": "13.0"
}
```

### Results:
- For benchmarks: `benchmark_results` with matmul, memory_bandwidth, compute_throughput
- For stress tests: `test_results` with compute/memory pass/fail status

---

## Testing Multiple GPUs

### Option 1: Test Specific GPU

Test a single GPU by specifying its ID:

```bash
# Benchmark GPU 0
python gpu_benchmarks/gpu_benchmark.py --gpu 0 --save

# Benchmark GPU 1
python gpu_benchmarks/gpu_benchmark.py --gpu 1 --save

# Stress test GPU 2
python gpu_benchmarks/gpu_stress_test.py --gpu 2 --duration 300 --save
```

### Option 2: Batch Test All GPUs

Use the batch testing script to test all GPUs automatically:

```bash
# Test all GPUs (benchmark + stress test)
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 300 --compare

# Benchmark only
python gpu_benchmarks/test_all_gpus.py --benchmark --compare

# Stress test only
python gpu_benchmarks/test_all_gpus.py --stress --duration 300 --compare

# Test specific GPUs
python gpu_benchmarks/test_all_gpus.py --gpus "0,2,3" --benchmark
```

### Option 3: Interactive Menu

Use the launcher script:

```bash
./gpu_benchmarks/run_benchmark.sh

# Then select:
# 20) List All Available GPUs
# 21) Test All GPUs (Benchmark + Stress)
# 22) Benchmark All GPUs
# 23) Stress Test All GPUs
# 24) Compare Results from Multiple GPUs
```

---

## Comparing Results

### Automatic Comparison (After Batch Test)

When using `--compare` flag with batch testing:

```bash
python gpu_benchmarks/test_all_gpus.py --benchmark --compare
```

This will:
1. Run benchmarks on all GPUs
2. Save individual results
3. Automatically generate comparison report

### Manual Comparison

Compare existing result files:

```bash
# Compare all benchmark results
python gpu_benchmarks/compare_results.py

# Save comparison to file
python gpu_benchmarks/compare_results.py --output comparison_report.txt

# Use custom file patterns
python gpu_benchmarks/compare_results.py --benchmark-pattern "benchmark_GPU*.json"

# Compare only specific types
python gpu_benchmarks/compare_results.py --benchmark-only
python gpu_benchmarks/compare_results.py --stress-only
```

---

## Comparison Report Format

The comparison tool generates detailed reports showing:

### 1. GPU Summary Table
Lists all tested GPUs with specs and test dates

### 2. Performance Comparisons

**Matrix Multiplication (GFLOPS):**
```
Size        GPU0 (RTX 3090)          GPU1 (RTX 4090)          GPU2 (RTX 3080)
1024x1024   18,584                   25,000                   15,000
2048x2048   22,181                   30,500                   18,200
...
```

**Memory Bandwidth (GB/s):**
```
Size (MB)   GPU0 (RTX 3090)          GPU1 (RTX 4090)
1           6.70                     7.50
10          8.41                     9.20
...
```

### 3. Best Performer Rankings
Shows which GPU performs best for each test

### 4. Stability Summary
Pass/fail status for all stress tests

---

## Example Workflows

### Workflow 1: Test 4 Different Cards

You have 4 different GPU models installed:

```bash
# Step 1: Identify GPUs
python -c "import torch; [print(f'GPU {i}: {torch.cuda.get_device_properties(i).name}') for i in range(torch.cuda.device_count())]"

# Step 2: Run full test suite on all GPUs
python gpu_benchmarks/test_all_gpus.py \
    --benchmark \
    --stress \
    --duration 600 \
    --compare

# Result: You'll get:
# - benchmark_GPU0_*.json
# - benchmark_GPU1_*.json
# - benchmark_GPU2_*.json
# - benchmark_GPU3_*.json
# - stress_test_GPU0_*.json
# - stress_test_GPU1_*.json
# - stress_test_GPU2_*.json
# - stress_test_GPU3_*.json
# - comparison_report_*.txt

# Step 3: Review comparison report
cat comparison_report_*.txt
```

### Workflow 2: Test Same Card in Different Systems

Testing the same GPU model in 4 different systems:

```bash
# On each system:
# System 1
python gpu_benchmarks/gpu_benchmark.py --gpu 0 --save
python gpu_benchmarks/gpu_stress_test.py --gpu 0 --duration 300 --save

# Copy result files to a central location:
# benchmark_GPU0_NVIDIA_GeForce_RTX_3090_system1_date.json
# stress_test_GPU0_NVIDIA_GeForce_RTX_3090_system1_date.json

# Repeat for systems 2, 3, 4...

# Compare all results:
python gpu_benchmarks/compare_results.py --output comparison_all_systems.txt
```

### Workflow 3: Before/After Comparison

Test GPU before and after changes (driver update, overclocking, etc.):

```bash
# Before changes
python gpu_benchmarks/gpu_benchmark.py --gpu 0 --save
# Save as: benchmark_before.json

# After changes
python gpu_benchmarks/gpu_benchmark.py --gpu 0 --save
# Save as: benchmark_after.json

# Compare (rename files to match pattern)
mv benchmark_GPU0_*.json results/
python gpu_benchmarks/compare_results.py --benchmark-pattern "results/*.json"
```

---

## Understanding Comparison Metrics

### Matrix Multiplication Performance (GFLOPS)
- **What it measures:** Raw compute performance
- **Higher is better**
- **Typical RTX 3090:** 20-26 TFLOPS
- **Use case:** Comparing compute capability across GPUs

### Memory Bandwidth (GB/s)
- **What it measures:** Data transfer speed between host and device
- **Higher is better**
- **Typical PCIe 4.0:** 7-9 GB/s (host-to-device)
- **Use case:** Identifying data transfer bottlenecks

### Compute Throughput (GOPS)
- **What it measures:** Element-wise operation speed
- **Higher is better**
- **Varies by operation:** Math functions faster than division
- **Use case:** Workload-specific optimization

### Stability Tests
- **PASSED:** GPU completed all iterations without errors
- **FAILED:** Detected NaN, Inf, crashes, or other errors
- **Use case:** Validating GPU reliability and stability

---

## Performance Ranking

The comparison tool automatically ranks GPUs by:
1. 8192x8192 matrix multiplication performance (primary metric)
2. Overall compute throughput
3. Memory bandwidth

Example output:
```
OVERALL PERFORMANCE RANKING (Based on 8192x8192 MatMul)

1. GPU1: NVIDIA GeForce RTX 4090
   Performance: 35,000 GFLOPS
   Memory: 24.00 GB | CUDA: 8.9

2. GPU0: NVIDIA GeForce RTX 3090
   Performance: 25,493 GFLOPS
   Memory: 24.00 GB | CUDA: 8.6

3. GPU2: NVIDIA GeForce RTX 3080
   Performance: 20,000 GFLOPS
   Memory: 10.00 GB | CUDA: 8.6
```

---

## Tips for Multi-GPU Testing

### 1. Test Sequentially
The batch test script automatically tests GPUs one at a time to avoid interference.

### 2. Consistent Test Parameters
Use the same test parameters (duration, matrix size) across all GPUs for fair comparison.

### 3. Cool-Down Periods
Allow GPUs to cool between tests for consistent thermal conditions:
```bash
# Test GPU 0
python gpu_benchmarks/gpu_benchmark.py --gpu 0 --save
sleep 60  # Cool down
# Test GPU 1
python gpu_benchmarks/gpu_benchmark.py --gpu 1 --save
```

### 4. Record System Configuration
Document:
- Driver version
- CUDA version
- System specs
- Cooling configuration
- Power limits

### 5. Multiple Runs
Run tests multiple times and compare results:
```bash
for i in {1..3}; do
    python gpu_benchmarks/test_all_gpus.py --benchmark
    sleep 300  # 5-minute cool down
done
```

### 6. Organize Results
Create directories for different test sessions:
```bash
mkdir -p results/session_20260122
mv benchmark_GPU*.json stress_test_GPU*.json results/session_20260122/
```

---

## Troubleshooting

### Different GPU Counts Show in Results
- Ensure all GPUs are properly detected: `nvidia-smi`
- Check CUDA visibility: `echo $CUDA_VISIBLE_DEVICES`

### Results Not Comparable
- Verify same PyTorch/CUDA versions across systems
- Check that tests used same parameters
- Ensure similar thermal conditions

### Comparison Script Finds No Files
- Check filename patterns match
- Verify files are in current directory
- Use `--benchmark-pattern` to specify custom paths

### Memory Errors During Batch Testing
- Increase cool-down between tests
- Reduce matrix size: `--matrix-size 4096`
- Test fewer GPUs at once: `--gpus "0,1"`

---

## Advanced Usage

### Custom Result Organization

```bash
# Create dated directory structure
TODAY=$(date +%Y%m%d)
mkdir -p results/$TODAY

# Run tests
python gpu_benchmarks/test_all_gpus.py --benchmark --stress

# Move results
mv benchmark_GPU*.json stress_test_GPU*.json results/$TODAY/

# Generate comparison
cd results/$TODAY
python ../../gpu_benchmarks/compare_results.py --output comparison.txt
```

### Scripted Multi-System Testing

```bash
#!/bin/bash
# test_all_systems.sh

SYSTEMS=("server1" "server2" "server3" "server4")

for system in "${SYSTEMS[@]}"; do
    echo "Testing $system..."
    ssh $system "cd /path/to/benchmarks && python gpu_benchmarks/gpu_benchmark.py --save"
    scp $system:/path/to/benchmarks/benchmark_GPU*.json ./results/${system}_
done

# Compare all results
python gpu_benchmarks/compare_results.py --benchmark-pattern "results/*" --output multi_system_comparison.txt
```

### Automated Reporting

```bash
#!/bin/bash
# daily_gpu_test.sh

# Run tests
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --compare

# Email report
DATE=$(date +%Y-%m-%d)
mail -s "Daily GPU Test Report - $DATE" admin@example.com < comparison_report_*.txt
```

---

## Summary

The enhanced multi-GPU benchmarking suite provides:

✅ **Clear GPU identification** in all output files
✅ **Structured data format** for easy parsing and analysis
✅ **Automated comparison** across multiple GPUs
✅ **Batch testing** for efficiency
✅ **Detailed reports** with rankings and summaries
✅ **Flexible workflows** for various testing scenarios

This makes it easy to:
- Test multiple GPUs in one system
- Compare the same GPU across different systems
- Track performance changes over time
- Identify the best performing GPU for your workload
- Validate GPU stability and reliability

For detailed usage of individual tools, see [README.md](README.md) and [QUICKSTART.md](QUICKSTART.md).
