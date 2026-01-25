# GPU Benchmarking - Quick Start Guide

## What You Have Installed

### Python Packages
- **gpustat** - Simple GPU monitoring tool
- **py3nvml** - NVIDIA Management Library Python bindings
- **nvidia-ml-py3** - NVIDIA ML metrics
- **PyTorch 2.9.1** - Already installed with CUDA 13.0 support

### Custom Tools Created
1. **gpu_monitor.py** - Real-time GPU monitoring dashboard
2. **gpu_stress_test.py** - Stability and stress testing
3. **gpu_benchmark.py** - Performance benchmarking suite
4. **run_benchmark.sh** - Interactive menu launcher

## Quickest Ways to Use

### 1. Interactive Menu (Easiest!)
```bash
./gpu_benchmarks/run_benchmark.sh
```
This launches an interactive menu with all options.

### 2. Quick GPU Check
```bash
source venv/bin/activate
gpustat
```

### 3. Real-Time Monitoring
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_monitor.py
```
Press Ctrl+C to stop.

### 4. Run Full Benchmark (Recommended First Test)
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_benchmark.py --save
```
This will:
- Test matrix multiplication performance
- Test memory bandwidth
- Test compute throughput
- Save results to JSON file

### 5. Stability Test (Recommended for New GPUs/Overclocks)
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_stress_test.py --duration 600
```
Runs a 10-minute stress test. Increase duration for longer tests.

## What Each Tool Does

### GPU Monitor
**Purpose:** Watch your GPU in real-time
**When to use:**
- During gaming/workloads to check temperatures
- To see if GPU is being utilized
- To monitor power consumption

**Example:**
```bash
python gpu_benchmarks/gpu_monitor.py 1
```

### GPU Benchmark
**Purpose:** Measure performance objectively
**When to use:**
- After building new PC
- Before/after overclocking
- Comparing different systems
- Verifying expected performance

**What it measures:**
- **GFLOPS** (Giga Floating Point Operations/Sec) - compute speed
- **GB/s** (Bandwidth) - data transfer speed
- **Latency** - operation time

**Your RTX 3090 Expected Performance:**
- Matrix multiplication: 20-30 TFLOPS
- Memory bandwidth: 25-30 GB/s (PCIe), ~900 GB/s (GPU internal)

### GPU Stress Test
**Purpose:** Verify stability under maximum load
**When to use:**
- Testing new GPU
- After overclocking
- Diagnosing crashes/instability
- Before important work/gaming sessions

**What it does:**
- Pushes GPU to 100% utilization
- Uses maximum memory
- Detects errors (NaN, Inf, crashes)
- Reports PASS/FAIL

**Recommended durations:**
- Quick test: 60 seconds
- Standard test: 10 minutes (600 seconds)
- Thorough test: 1 hour (3600 seconds)
- Burn-in: 24 hours (86400 seconds)

## Common Scenarios

### "I just want to see if my GPU is working well"
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_benchmark.py --save
python gpu_benchmarks/gpu_stress_test.py --duration 300
```
This runs a benchmark and 5-minute stability test.

### "I overclocked my GPU and want to test stability"
```bash
source venv/bin/activate
# Run stress test while monitoring in another terminal
# Terminal 1:
python gpu_benchmarks/gpu_stress_test.py --duration 3600

# Terminal 2:
python gpu_benchmarks/gpu_monitor.py 1
```
Watch for:
- Temperature < 85°C (ideally < 80°C)
- No errors in stress test
- Stable clocks (not throttling)

### "My GPU seems slow, I want to benchmark it"
```bash
source venv/bin/activate
python gpu_benchmarks/gpu_benchmark.py --test matmul
```
Compare results to expected RTX 3090 performance (20-30 TFLOPS).

### "I want to monitor GPU during a long task"
```bash
source venv/bin/activate
# Run this in a separate terminal while your task runs
python gpu_benchmarks/gpu_monitor.py 2
```

## Understanding Results

### Benchmark Results

**Good RTX 3090 Performance:**
- Matrix multiplication: 20-30 TFLOPS (GFLOPS in thousands)
- Memory bandwidth: 25-32 GB/s (PCIe)
- GPU utilization: Near 100% during test

**Low Performance Indicators:**
- GFLOPS < 15,000
- High latency
- Low GPU utilization
- Thermal throttling

### Stress Test Results

**PASSED:**
- All iterations completed
- No NaN or Inf errors
- No crashes
- Stable temperatures

**FAILED:**
- NaN or Inf detected - memory or compute errors
- Crashes - stability issues
- Thermal throttling - cooling problems

## Monitoring Tips

### Watch These Metrics

1. **Temperature**
   - Idle: 40-50°C
   - Load: 65-80°C (good)
   - Load: 80-85°C (acceptable)
   - Load: >85°C (reduce load/improve cooling)

2. **Power**
   - RTX 3090 TDP: 350-420W
   - Should reach near-limit during stress tests
   - Low power during load = throttling

3. **Clock Speeds**
   - Boost: 1700-1900+ MHz (varies by card)
   - If clocks drop during load = throttling

4. **Memory**
   - RTX 3090 has 24GB
   - Monitor usage for your workloads

### Signs of Problems

- **Thermal throttling:** Temps >83°C, clocks dropping
- **Power throttling:** Not reaching TDP, performance drop
- **Memory issues:** Errors in stress test, artifacts
- **Unstable overclock:** Crashes, errors, artifacts

## Built-in NVIDIA Tools

### nvidia-smi
```bash
# Simple check
nvidia-smi

# Continuous monitoring
watch -n 1 nvidia-smi

# Query specific info
nvidia-smi --query-gpu=temperature.gpu,power.draw,utilization.gpu --format=csv
```

### gpustat
```bash
# Simple view
gpustat

# Continuous (1 second updates)
gpustat -i 1

# With CPU info
gpustat -cpu
```

## Files Location

All tools are in: `gpu_benchmarks/`

```
gpu_benchmarks/
├── gpu_monitor.py          # Real-time monitoring
├── gpu_stress_test.py      # Stability testing
├── gpu_benchmark.py        # Performance benchmarking
├── run_benchmark.sh        # Interactive menu
├── README.md              # Detailed documentation
└── QUICKSTART.md          # This file
```

## Next Steps

1. **First time:** Run full benchmark to establish baseline
   ```bash
   source venv/bin/activate
   python gpu_benchmarks/gpu_benchmark.py --save
   ```

2. **Regular monitoring:** Use the interactive menu
   ```bash
   ./gpu_benchmarks/run_benchmark.sh
   ```

3. **Stability check:** Run stress test
   ```bash
   source venv/bin/activate
   python gpu_benchmarks/gpu_stress_test.py --duration 600
   ```

## Need Help?

- Check [README.md](README.md) for detailed documentation
- All scripts have `--help` option:
  ```bash
  python gpu_benchmarks/gpu_benchmark.py --help
  ```

## Your System Info

- **GPU:** NVIDIA GeForce RTX 3090
- **VRAM:** 24GB
- **Driver:** 590.48.01
- **CUDA:** 13.1
- **PyTorch:** 2.9.1+cu130
