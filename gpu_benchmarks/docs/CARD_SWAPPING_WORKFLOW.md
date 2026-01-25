# Card Swapping Workflow - Testing Multiple GPUs Sequentially

## Your Use Case

You're testing **4 different GPU cards sequentially** by:
1. Shutting down
2. Swapping the physical GPU card
3. Rebooting
4. Running benchmarks on the new card
5. Repeat for each card

**The suite automatically handles this** - it detects whatever GPU is in slot 0 and saves results with GPU-specific filenames so nothing gets overwritten.

---

## Quick Workflow

### For Each Card:

```bash
# 1. Shutdown and swap card physically
# 2. Boot up
# 3. Run the full test suite

source venv/bin/activate
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600 --compare
```

That's it! The script will:
- Auto-detect the GPU in the system
- Test it (even if it's GPU 0, GPU 1, or multiple GPUs)
- Save with GPU-specific filename: `benchmark_GPU0_[CardName]_[timestamp].json`
- Each card swap creates new files, nothing gets overwritten

---

## Filename Format Prevents Overwriting

### Files Created Per Card:

**Card 1 (EVGA RTX 3090 XC3 ULTRA):**
```
benchmark_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143025.json
stress_test_GPU0_NVIDIA_GeForce_RTX_3090_20260122_143530.json
gpu_identification_GPU0_20260122_143010.json
```

**Card 2 (EVGA RTX 4090 FTW3 ULTRA) - After swap:**
```
benchmark_GPU0_NVIDIA_GeForce_RTX_4090_20260122_153025.json
stress_test_GPU0_NVIDIA_GeForce_RTX_4090_20260122_153530.json
gpu_identification_GPU0_20260122_153010.json
```

**Card 3, Card 4, etc.** - All get unique filenames because:
- Different GPU names
- Different timestamps
- Both prevent overwriting

---

## Step-by-Step: Testing 4 Cards

### Card 1: EVGA RTX 3090 XC3 ULTRA

```bash
# 1. Install card, boot system
# 2. Verify it's detected
nvidia-smi

# 3. Identify the card
source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0 --save

# 4. Run full benchmark and stress test
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600 --compare

# Results saved:
# - benchmark_GPU0_NVIDIA_GeForce_RTX_3090_YYYYMMDD_HHMMSS.json
# - stress_test_GPU0_NVIDIA_GeForce_RTX_3090_YYYYMMDD_HHMMSS.json
```

### Card 2: EVGA RTX 4090 FTW3 ULTRA

```bash
# 1. Shutdown system
sudo shutdown -h now

# 2. Swap card physically (remove 3090, install 4090)

# 3. Boot system

# 4. Verify new card
nvidia-smi

# 5. Run tests (same commands)
source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600 --compare

# Results saved (different filename):
# - benchmark_GPU0_NVIDIA_GeForce_RTX_4090_YYYYMMDD_HHMMSS.json
# - stress_test_GPU0_NVIDIA_GeForce_RTX_4090_YYYYMMDD_HHMMSS.json
```

### Card 3 & 4: Repeat

Same process - each card gets unique filenames automatically.

---

## After Testing All Cards

### Compare All Results

```bash
source venv/bin/activate
python gpu_benchmarks/compare_results.py --output comparison_all_cards.txt
```

This compares all the JSON files and shows:
- Performance comparison table
- Rankings
- Best performer for each metric
- Stability summary

### Example Comparison Output:

```
================================================================================
BENCHMARK RESULTS COMPARISON
================================================================================

GPU SUMMARY:
ID    GPU Name                     Memory      CUDA    Test Date
0     EVGA RTX 3090 XC3 ULTRA      24.00 GB    8.6     2026-01-22
0     EVGA RTX 4090 FTW3 ULTRA     24.00 GB    8.9     2026-01-22
0     ASUS RTX 3080 TUF GAMING     10.00 GB    8.6     2026-01-22
0     MSI RTX 3070 GAMING X        8.00 GB     8.6     2026-01-23

MATRIX MULTIPLICATION PERFORMANCE (GFLOPS)

Size        RTX 3090 XC3    RTX 4090 FTW3   RTX 3080 TUF    RTX 3070
1024x1024   18,584          32,000          15,000          12,000
2048x2048   22,181          38,500          18,200          14,500
8192x8192   25,493          52,000          22,100          17,800

OVERALL PERFORMANCE RANKING:
1. EVGA RTX 4090 FTW3 ULTRA - 52,000 GFLOPS
2. EVGA RTX 3090 XC3 ULTRA - 25,493 GFLOPS
3. ASUS RTX 3080 TUF GAMING - 22,100 GFLOPS
4. MSI RTX 3070 GAMING X - 17,800 GFLOPS
```

---

## Best Practices for Card Swapping

### 1. Always Shutdown Properly
```bash
sudo shutdown -h now
```
Never hot-swap GPUs!

### 2. Identify Each Card First
```bash
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
```
This creates a record of exactly which card you tested.

### 3. Use Consistent Test Parameters
For fair comparison, use same settings for all cards:
```bash
# Same duration
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600

# Same matrix size (if testing individually)
python gpu_benchmarks/gpu_stress_test.py --duration 600 --matrix-size 8192
```

### 4. Organize Results by Session
```bash
# Create directories for each card
mkdir -p results/card1_rtx3090_xc3
mkdir -p results/card2_rtx4090_ftw3
mkdir -p results/card3_rtx3080_tuf
mkdir -p results/card4_rtx3070_gaming

# Move results after each test
mv benchmark_GPU0_*.json stress_test_GPU0_*.json gpu_identification_*.json results/card1_rtx3090_xc3/
```

### 5. Document Each Card
Keep notes:
```bash
# Create info file for each card
cat > results/card1_rtx3090_xc3/notes.txt << EOF
Card: EVGA RTX 3090 XC3 ULTRA
Purchase Date: 2021-10-15
Serial Number: XXX
VBIOS: 94.02.42.C0.05
Test Date: 2026-01-22
Condition: Used, excellent
EOF
```

---

## Automatic Multi-GPU Detection

The suite **automatically adapts** to your system:

### Single GPU (Most Common for You):
```bash
python gpu_benchmarks/test_all_gpus.py --benchmark

# Output:
# Found 1 GPU(s):
# GPU 0: NVIDIA GeForce RTX 3090
# Testing 1 GPU(s): [0]
# [Tests GPU 0 only]
```

### Multiple GPUs (If Present):
```bash
python gpu_benchmarks/test_all_gpus.py --benchmark

# Output:
# Found 3 GPU(s):
# GPU 0: NVIDIA GeForce RTX 3090
# GPU 1: NVIDIA GeForce RTX 3080
# GPU 2: NVIDIA GeForce RTX 3070
# Testing 3 GPU(s): [0, 1, 2]
# [Tests all 3 GPUs]
```

So the same command works whether you have 1 or multiple cards!

---

## Interactive Menu

The launcher script also works:

```bash
./gpu_benchmarks/run_benchmark.sh

# Select:
# 20) List All Available GPUs      <- See what's detected
# 21) Test All GPUs                <- Test whatever's present
# 24) Compare Results              <- Compare all saved results
```

---

## Troubleshooting Card Swaps

### Issue: New Card Not Detected

**Solution:**
```bash
# Check if system sees it
lspci | grep VGA

# Check if driver sees it
nvidia-smi

# If not, may need driver reload
sudo rmmod nvidia_uvm nvidia_drm nvidia_modeset nvidia
sudo modprobe nvidia
```

### Issue: Old Card Name Still Showing

**Solution:**
This shouldn't happen if you properly shutdown, but if it does:
```bash
# Clear CUDA cache
sudo rm -rf /tmp/cuda_*

# Reboot
sudo reboot
```

### Issue: Files Getting Overwritten

**Solution:**
This shouldn't happen because filenames include GPU name + timestamp. But if you run tests very quickly (same timestamp), add manual suffix:
```bash
# For card 1
python gpu_benchmarks/test_all_gpus.py --benchmark
mv benchmark_GPU0_*.json benchmark_GPU0_card1_*.json

# For card 2
python gpu_benchmarks/test_all_gpus.py --benchmark
mv benchmark_GPU0_*.json benchmark_GPU0_card2_*.json
```

---

## Summary

### Your Workflow is Simple:

1. **Swap card** (shutdown, swap, boot)
2. **Run tests**: `python gpu_benchmarks/test_all_gpus.py --benchmark --stress --compare`
3. **Repeat** for each card
4. **Compare all**: `python gpu_benchmarks/compare_results.py`

### Why It Works:

✅ **Auto-detects** whatever GPU is in the system
✅ **GPU-specific filenames** prevent overwriting
✅ **Timestamp in filename** prevents conflicts
✅ **Flexible** - works with 1 GPU or multiple
✅ **Comparison tool** handles all saved results

### File Naming Ensures Safety:

```
benchmark_GPU{id}_{GPU_NAME}_{timestamp}.json
         ^^^^       ^^^^^^^^   ^^^^^^^^^
         |          |          └─ Unique timestamp
         |          └─ Card-specific name
         └─ GPU slot (usually 0)
```

Each card swap creates completely new files. Nothing gets overwritten!

---

## Quick Commands Reference

```bash
# Activate environment
source venv/bin/activate

# Identify current card
python gpu_benchmarks/identify_gpu.py --gpu 0 --save

# Quick benchmark only
python gpu_benchmarks/test_all_gpus.py --benchmark

# Full test (benchmark + 10min stress)
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600

# Full test with comparison
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600 --compare

# Compare all saved results
python gpu_benchmarks/compare_results.py

# Compare and save report
python gpu_benchmarks/compare_results.py --output my_card_comparison.txt

# Interactive menu
./gpu_benchmarks/run_benchmark.sh
```

---

## Example Complete Session

```bash
# ============ Card 1: RTX 3090 XC3 ULTRA ============
# (Physical install, boot)

source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600

# (Shutdown when tests complete)
sudo shutdown -h now

# ============ Card 2: RTX 4090 FTW3 ULTRA ============
# (Physical swap, boot)

source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600

sudo shutdown -h now

# ============ Card 3: RTX 3080 TUF GAMING ============
# (Physical swap, boot)

source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600

sudo shutdown -h now

# ============ Card 4: RTX 3070 GAMING X ============
# (Physical swap, boot)

source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
python gpu_benchmarks/test_all_gpus.py --benchmark --stress --duration 600

# ============ Compare All Results ============
python gpu_benchmarks/compare_results.py --output final_comparison.txt
cat final_comparison.txt
```

You now have complete benchmarks and comparison for all 4 cards!
