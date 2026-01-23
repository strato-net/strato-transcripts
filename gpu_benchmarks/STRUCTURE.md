# GPU Benchmarking Suite - Directory Structure

## Overview

```
gpu_benchmarks/
├── benchmark              # Main launcher (run this!)
├── README.md             # Quick start guide
├── STRUCTURE.md          # This file
├── .gitignore            # Git ignore rules
│
├── scripts/              # All executable scripts
│   ├── identify_gpu.py           # GPU model identification
│   ├── gpu_benchmark.py          # Performance benchmarking
│   ├── gpu_stress_test.py        # Stability testing
│   ├── test_all_gpus.py          # Batch testing all GPUs
│   ├── compare_results.py        # Results comparison
│   ├── gpu_monitor.py            # Real-time monitoring
│   └── run_benchmark.sh          # Interactive menu
│
├── docs/                 # Documentation
│   ├── README.md                 # Detailed documentation
│   ├── QUICKSTART.md             # Quick reference
│   ├── CARD_SWAPPING_WORKFLOW.md # Card-swapping guide
│   ├── GPU_IDENTIFICATION_GUIDE.md # GPU ID guide
│   ├── MULTI_GPU_GUIDE.md        # Multi-GPU testing
│   ├── CHANGES_MULTI_GPU.md      # Change log
│   └── TEST_RESULTS_20260122.md  # Example results
│
└── results/              # Test results directory
    └── archive/          # Archive old results
```

## File Descriptions

### Root Level

**`benchmark`** - Main launcher script
- Activates virtual environment
- Launches interactive menu
- **Usage:** `./benchmark`

**`README.md`** - Quick start guide
- Overview and quick commands
- Directory structure
- Basic usage examples

**`.gitignore`** - Git ignore rules
- Ignores JSON result files
- Ignores Python cache
- Ignores comparison reports

### scripts/ - Executable Scripts

**`identify_gpu.py`** - GPU Model Identification
- Identifies exact GPU model (EVGA FTW3, ASUS ROG Strix, etc.)
- Determines manufacturer and variant
- Exports to JSON
- **Usage:** `python scripts/identify_gpu.py --gpu 0 --save`

**`gpu_benchmark.py`** - Performance Benchmarking
- Matrix multiplication (GFLOPS)
- Memory bandwidth (GB/s)
- Compute throughput (GOPS)
- **Usage:** `python scripts/gpu_benchmark.py --save`

**`gpu_stress_test.py`** - Stability Testing
- Compute stress test
- Memory stress test
- Error detection
- **Usage:** `python scripts/gpu_stress_test.py --duration 600 --save`

**`test_all_gpus.py`** - Batch Testing
- Auto-detects all GPUs
- Tests sequentially
- Generates comparison
- **Usage:** `python scripts/test_all_gpus.py --benchmark --stress --compare`

**`compare_results.py`** - Results Comparison
- Compares multiple GPU results
- Side-by-side performance tables
- Rankings and best performers
- **Usage:** `python scripts/compare_results.py --output results/comparison.txt`

**`gpu_monitor.py`** - Real-time Monitoring
- Live GPU stats dashboard
- Temperature, power, utilization
- Clock speeds and memory
- **Usage:** `python scripts/gpu_monitor.py`

**`run_benchmark.sh`** - Interactive Menu
- Text-based menu interface
- All tools in one place
- Guided workflow
- **Usage:** `./scripts/run_benchmark.sh` or `./benchmark`

### docs/ - Documentation

**`README.md`** - Detailed Documentation
- Complete tool descriptions
- All features explained
- Troubleshooting guide

**`QUICKSTART.md`** - Quick Reference
- Common commands
- Quick examples
- Installation check

**`CARD_SWAPPING_WORKFLOW.md`** - Card Swapping Guide
- Sequential card testing workflow
- Step-by-step instructions
- Best practices
- **Your primary workflow guide**

**`GPU_IDENTIFICATION_GUIDE.md`** - GPU Identification
- Agent instructions for identifying GPUs
- Model database reference
- Manual identification process
- Acts like a "skill" for AI agents

**`MULTI_GPU_GUIDE.md`** - Multi-GPU Testing
- Multi-GPU feature guide
- Comparison workflows
- Batch testing instructions

**`CHANGES_MULTI_GPU.md`** - Change Log
- Multi-GPU enhancement details
- Implementation notes
- Migration guide

**`TEST_RESULTS_20260122.md`** - Example Results
- Sample test report
- Performance analysis
- Interpretation guide

### results/ - Results Directory

**Where test results are saved:**

Results are automatically saved to the parent directory with GPU-specific filenames:
```
../benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143025.json
../stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143530.json
../gpu_identification_GPU0_20260122_143010.json
```

**Recommended practice:** Move results here after testing:
```bash
# Move current results
mv ../benchmark_*.json ../stress_test_*.json ../gpu_identification_*.json results/

# Archive old results
mv results/benchmark_*.json results/archive/
```

**`results/archive/`** - Old results storage
- Keep history of past tests
- Compare over time
- Track performance changes

## Usage Patterns

### Quick Start

```bash
# Easiest - interactive menu
./benchmark

# Direct - test current GPU
python scripts/test_all_gpus.py --benchmark --stress --duration 600 --compare
```

### Card Swapping Workflow

```bash
# For each card:
# 1. Shutdown, swap card, boot
# 2. Run tests
python scripts/identify_gpu.py --gpu 0 --save
python scripts/test_all_gpus.py --benchmark --stress --duration 600

# After all cards:
python scripts/compare_results.py --output results/comparison_all_cards.txt
```

### Individual Tools

```bash
# Identify GPU
python scripts/identify_gpu.py --gpu 0

# Benchmark only
python scripts/gpu_benchmark.py --save

# Stress test only
python scripts/gpu_stress_test.py --duration 600 --test compute --save

# Monitor
python scripts/gpu_monitor.py

# Compare results
python scripts/compare_results.py
```

## Path References

When running scripts, paths are relative to where you run them:

**From project root:**
```bash
python gpu_benchmarks/scripts/identify_gpu.py --gpu 0
```

**From gpu_benchmarks/:**
```bash
python scripts/identify_gpu.py --gpu 0
./benchmark
```

**From anywhere (using full path):**
```bash
python /home/cudatiger/Projects/strato-transcripts/gpu_benchmarks/scripts/identify_gpu.py --gpu 0
```

## Result Filenames

Auto-generated filenames follow this pattern:

**Benchmarks:**
```
benchmark_GPU{id}_{GPU_Name}_{YYYYMMDD_HHMMSS}.json
```
Example: `benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143025.json`

**Stress Tests:**
```
stress_test_GPU{id}_{GPU_Name}_{YYYYMMDD_HHMMSS}.json
```
Example: `stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143530.json`

**Identifications:**
```
gpu_identification_GPU{id}_{YYYYMMDD_HHMMSS}.json
```
Example: `gpu_identification_GPU0_20260122_143010.json`

**Comparisons:**
```
comparison_report_{YYYYMMDD_HHMMSS}.txt
```
Example: `comparison_report_20260122_150530.txt`

## Organization Tips

### Create dated directories
```bash
mkdir -p results/2026-01-22
mv benchmark_*.json stress_test_*.json results/2026-01-22/
```

### Organize by card
```bash
mkdir -p results/rtx3090_xc3 results/rtx4090_ftw3
mv benchmark_*RTX_3090*.json results/rtx3090_xc3/
mv benchmark_*RTX_4090*.json results/rtx4090_ftw3/
```

### Archive old results
```bash
# Archive results older than 30 days
find results/ -name "*.json" -mtime +30 -exec mv {} results/archive/ \;
```

## Maintenance

### Clean up old results
```bash
# Move all JSON files to results
mv ../*.json results/ 2>/dev/null

# Archive old results
mv results/*.json results/archive/ 2>/dev/null
```

### Update documentation
Documentation in `docs/` can be edited as needed. The main launcher and scripts reference these files.

### Add new scripts
New Python scripts go in `scripts/`. Make them executable:
```bash
chmod +x scripts/new_script.py
```

## Integration

### With version control
The `.gitignore` is configured to:
- ✅ Track all scripts and documentation
- ❌ Ignore JSON result files
- ❌ Ignore Python cache
- ❌ Ignore comparison reports

### With other projects
The suite is self-contained in `gpu_benchmarks/`. You can:
- Copy entire directory to other systems
- Share scripts independently
- Export results for analysis elsewhere

## Summary

**Main Entry Point:** `./benchmark`

**Core Scripts:** `scripts/*.py`

**Documentation:** `docs/*.md`

**Results:** Save to `results/` directory

**Your Workflow:** See `docs/CARD_SWAPPING_WORKFLOW.md`
