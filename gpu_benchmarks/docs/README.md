# GPU Benchmarking and Stability Testing Suite

Comprehensive tools for benchmarking and stress testing NVIDIA GPUs with multi-GPU support and comparison capabilities.

## New: Multi-GPU Support

The benchmarking suite now supports testing and comparing multiple GPUs:
- **GPU-specific result files** with GPU ID and name in filenames
- **Batch testing** - test all GPUs automatically
- **Comparison tool** - compare performance across multiple GPUs
- **Automated reporting** with rankings and summaries

See [MULTI_GPU_GUIDE.md](MULTI_GPU_GUIDE.md) for detailed multi-GPU testing instructions.

## Tools Included

### 1. GPU Monitor (`gpu_monitor.py`)
Real-time GPU monitoring dashboard showing:
- Temperature
- Power usage
- Fan speed
- GPU and memory utilization
- Clock speeds
- Memory usage

**Usage:**
```bash
# Monitor with default 1-second interval
python gpu_monitor.py

# Custom interval (2 seconds)
python gpu_monitor.py 2

# Monitor for specific duration (60 seconds with 1-second interval)
python gpu_monitor.py 1 60
```

### 2. GPU Stress Test (`gpu_stress_test.py`)
Intensive stability testing to verify GPU reliability under load:
- Matrix multiplication stress test
- Memory allocation/deallocation stress test
- Error detection and reporting

**Usage:**
```bash
# Run all stress tests for 60 seconds
python gpu_stress_test.py

# Run compute stress test only for 300 seconds (5 minutes)
python gpu_stress_test.py --test compute --duration 300

# Run memory stress test
python gpu_stress_test.py --test memory --duration 120

# Specify GPU and matrix size
python gpu_stress_test.py --gpu 0 --matrix-size 10000 --duration 600
```

**Options:**
- `--gpu`: GPU ID to test (default: 0)
- `--duration`: Test duration in seconds (default: 60)
- `--matrix-size`: Matrix dimension for compute test (default: 8192)
- `--test`: Test type - `compute`, `memory`, or `all` (default: all)
- `--save`: Save results to JSON file

**New:** Results are saved with GPU-specific filenames:
- Format: `stress_test_GPU{id}_{gpu_name}_{timestamp}.json`
- Example: `stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_200151.json`

### 3. GPU Benchmark (`gpu_benchmark.py`)
Performance benchmarking suite measuring:
- Matrix multiplication performance (GFLOPS)
- Memory bandwidth (host-to-device and device-to-host)
- Compute throughput for various operations

**Usage:**
```bash
# Run full benchmark suite
python gpu_benchmark.py

# Run specific benchmark
python gpu_benchmark.py --test matmul
python gpu_benchmark.py --test memory
python gpu_benchmark.py --test compute

# Save results to JSON file
python gpu_benchmark.py --save

# Specify GPU
python gpu_benchmark.py --gpu 0
```

**Options:**
- `--gpu`: GPU ID to benchmark (default: 0)
- `--test`: Benchmark type - `matmul`, `memory`, `compute`, or `all` (default: all)
- `--save`: Save results to JSON file

**New:** Results are saved with GPU-specific filenames:
- Format: `benchmark_GPU{id}_{gpu_name}_{timestamp}.json`
- Example: `benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_195914.json`

### 4. Multi-GPU Batch Testing (`test_all_gpus.py`)
Test all available GPUs automatically with comparison reporting.

**Usage:**
```bash
# Test all GPUs (benchmark + stress test)
python test_all_gpus.py --benchmark --stress --duration 300 --compare

# Benchmark all GPUs only
python test_all_gpus.py --benchmark --compare

# Test specific GPUs
python test_all_gpus.py --gpus "0,2,3" --benchmark
```

**Options:**
- `--gpus`: Comma-separated list of GPU IDs (default: all)
- `--benchmark`: Run benchmarks
- `--stress`: Run stress tests
- `--duration`: Stress test duration (default: 60)
- `--compare`: Generate comparison report after tests

### 5. Results Comparison Tool (`compare_results.py`)
Compare benchmark and stress test results across multiple GPUs.

**Usage:**
```bash
# Compare all results
python compare_results.py

# Save comparison to file
python compare_results.py --output comparison_report.txt

# Compare only benchmarks or stress tests
python compare_results.py --benchmark-only
python compare_results.py --stress-only
```

**Features:**
- Side-by-side performance comparison tables
- Best performer identification
- Performance rankings
- Stability summary across all GPUs

## Quick Start

### Installation
All required packages are installed:
```bash
source venv/bin/activate
```

Packages:
- `gpustat` - GPU monitoring
- `py3nvml` - NVIDIA Management Library
- `nvidia-ml-py3` - NVIDIA ML Python bindings
- `torch` - PyTorch with CUDA support

### Quick Monitor
```bash
# Real-time monitoring
source venv/bin/activate
python gpu_benchmarks/gpu_monitor.py

# Or use gpustat
gpustat -i 1
```

### Run Stability Test
```bash
source venv/bin/activate
# 10-minute stress test
python gpu_benchmarks/gpu_stress_test.py --duration 600
```

### Run Performance Benchmark
```bash
source venv/bin/activate
# Full benchmark with saved results
python gpu_benchmarks/gpu_benchmark.py --save
```

## Understanding Results

### Stress Test
- **PASSED**: GPU completed all operations without errors
- **FAILED**: Detected NaN, Inf, or runtime errors (potential stability issues)

Common failure causes:
- Overheating (check temperature)
- Power limit throttling
- Memory errors
- Unstable overclock

### Benchmark Results

**Matrix Multiplication:**
- GFLOPS = Giga Floating Point Operations Per Second
- Higher is better
- RTX 3090 theoretical peak: ~35 TFLOPS FP32

**Memory Bandwidth:**
- GB/s = Gigabytes per second
- PCIe 4.0 x16 theoretical: ~32 GB/s
- GPU memory bandwidth (RTX 3090): ~936 GB/s (internal)

**Compute Throughput:**
- GOPS = Giga Operations Per Second
- Varies by operation complexity
- Higher is better

## Monitoring During Tests

Open two terminals:

**Terminal 1 - Run test:**
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_stress_test.py --duration 600
```

**Terminal 2 - Monitor:**
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_monitor.py 1
```

## Troubleshooting

### GPU Too Hot
- Improve case airflow
- Check dust in heatsink
- Adjust fan curve
- Reduce power limit

### Power Throttling
- Check PSU capacity
- Increase power limit if safe
- Monitor with: `nvidia-smi -q -d POWER`

### Memory Errors
- Test with smaller matrix sizes
- Check for GPU memory issues
- May indicate hardware problems

### Low Performance
- Check for background processes
- Verify GPU is not throttling
- Update NVIDIA drivers
- Check PCIe link: `nvidia-smi -q | grep "Link Width"`

## Advanced Usage

### Custom Monitoring Script
```python
from gpu_monitor import GPUMonitor

monitor = GPUMonitor()
info = monitor.get_gpu_info(gpu_id=0)
print(f"Temperature: {info['temperature']}°C")
```

### Continuous Monitoring to File
```bash
# Log GPU stats every second
while true; do
    nvidia-smi --query-gpu=timestamp,temperature.gpu,power.draw,utilization.gpu,memory.used \
    --format=csv >> gpu_log.csv
    sleep 1
done
```

## System Tools

### Built-in NVIDIA Tools
```bash
# Basic monitoring
nvidia-smi

# Continuous monitoring (1 second interval)
watch -n 1 nvidia-smi

# Query specific metrics
nvidia-smi --query-gpu=name,temperature.gpu,utilization.gpu,memory.used --format=csv

# Detailed device info
nvidia-smi -q

# Power and temperature monitoring
nvidia-smi dmon -s pucvmet
```

### Using gpustat
```bash
# Simple view
gpustat

# Continuous monitoring
gpustat -i 1

# Show all processes
gpustat -cpu
```

## Notes

- Stress tests may drive GPU to thermal limits - monitor temperatures
- Long stress tests (1+ hours) recommended for stability validation
- Benchmark results vary with GPU boost behavior
- Close other GPU applications for accurate benchmarks
- Run multiple iterations for consistent results
