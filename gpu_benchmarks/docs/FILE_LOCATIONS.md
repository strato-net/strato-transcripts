# File Locations - Quick Reference

## Where Everything Is

### Result Files (JSON)
All test results are in: **`gpu_benchmarks/results/`**

```
gpu_benchmarks/results/
├── benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_195914.json
├── benchmark_results_20260122_192319.json
├── gpu_identification_GPU0_20260122_201155.json
├── stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_200151.json
└── archive/          # Move old results here
    └── .gitkeep
```

### Documentation Files
All documentation is in: **`gpu_benchmarks/docs/`**

```
gpu_benchmarks/docs/
├── CARD_SWAPPING_WORKFLOW.md         # Your workflow guide
├── CHANGES_MULTI_GPU.md              # Change log
├── GPU_IDENTIFICATION_GUIDE.md       # GPU ID agent instructions
├── GPU_IDENTIFICATION_SAVED.md       # Your current GPU details
├── MULTI_GPU_GUIDE.md                # Multi-GPU features
├── MULTI_GPU_READY.md                # Multi-GPU summary
├── QUICKSTART.md                     # Quick reference
├── README.md                         # Detailed documentation
└── TEST_RESULTS_20260122.md          # Example results
```

### Scripts (Python & Shell)
All executable tools are in: **`gpu_benchmarks/scripts/`**

```
gpu_benchmarks/scripts/
├── identify_gpu.py          # GPU model identification
├── gpu_benchmark.py         # Performance benchmarking
├── gpu_stress_test.py       # Stability testing
├── test_all_gpus.py         # Batch testing
├── compare_results.py       # Results comparison
├── gpu_monitor.py           # Real-time monitoring
└── run_benchmark.sh         # Interactive menu
```

### Root Level
**`gpu_benchmarks/`** directory contains:

```
gpu_benchmarks/
├── benchmark              # Main launcher (run this!)
├── README.md             # Quick start guide
├── STRUCTURE.md          # Directory structure guide
├── .gitignore            # Git ignore rules
├── results/              # Results directory
├── docs/                 # Documentation directory
└── scripts/              # Scripts directory
```

## Quick Access

### From Project Root
```bash
cd /home/cudatiger/Projects/strato-transcripts

# Run benchmarks
./gpu_benchmarks/benchmark

# Or:
cd gpu_benchmarks && ./benchmark
```

### From gpu_benchmarks/
```bash
cd gpu_benchmarks

# Main launcher
./benchmark

# Direct commands
python scripts/identify_gpu.py --gpu 0
python scripts/test_all_gpus.py --benchmark --stress
python scripts/compare_results.py

# View results
ls results/
cat results/benchmark_*.json

# Read docs
cat docs/CARD_SWAPPING_WORKFLOW.md
```

## File Naming Patterns

**Benchmark results:**
```
benchmark_GPU{id}_{GPU_Name}_{YYYYMMDD_HHMMSS}.json
```

**Stress test results:**
```
stress_test_GPU{id}_{GPU_Name}_{YYYYMMDD_HHMMSS}.json
```

**GPU identification:**
```
gpu_identification_GPU{id}_{YYYYMMDD_HHMMSS}.json
```

**Comparison reports:**
```
comparison_report_{YYYYMMDD_HHMMSS}.txt
```

## Organization Tips

### View all results
```bash
ls -lh gpu_benchmarks/results/
```

### Archive old results
```bash
mv gpu_benchmarks/results/*.json gpu_benchmarks/results/archive/
```

### Find specific card results
```bash
ls gpu_benchmarks/results/*RTX_3090*.json
ls gpu_benchmarks/results/*RTX_4090*.json
```

### Compare all results
```bash
python gpu_benchmarks/scripts/compare_results.py \
  --output gpu_benchmarks/results/comparison.txt
```

## Current File Inventory

As of cleanup (2026-01-22):

**Results:** 4 JSON files
- benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_195914.json
- benchmark_results_20260122_192319.json
- gpu_identification_GPU0_20260122_201155.json
- stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_200151.json

**Documentation:** 9 markdown files
**Scripts:** 7 executable files

Total organized: **20 files** in proper locations

## What Was Moved

During cleanup, the following were moved from root to proper locations:

**From root → gpu_benchmarks/results/**
- benchmark_GPU0_*.json
- benchmark_results_*.json
- gpu_identification_*.json
- stress_test_GPU0_*.json

**From root → gpu_benchmarks/docs/**
- GPU_IDENTIFICATION_SAVED.md
- MULTI_GPU_READY.md

**Removed:**
- Misplaced `results/` directory in root

## Root Directory (Clean)

Project root now only contains:
- LICENSE
- README.md (project README)
- requirements.txt
- setup_env.sh
- WORKAROUNDS.md
- gpu_benchmarks/ (organized suite)
- intermediates/ (transcripts)
- outputs/ (transcripts)
- venv/ (Python environment)
- scripts/ (transcript scripts)

Everything GPU-related is inside `gpu_benchmarks/` directory.

---

**Remember:** All GPU benchmarking files belong in `gpu_benchmarks/` subdirectories!
