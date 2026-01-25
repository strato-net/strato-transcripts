# GPU Identification - Saved Information

**Date:** 2026-01-22 20:11:55
**System:** /home/cudatiger/Projects/strato-transcripts

---

## Your GPU

### Exact Model: **EVGA GeForce RTX 3090 XC3 ULTRA GAMING**

### Complete Specifications

| Category | Details |
|----------|---------|
| **Manufacturer** | EVGA |
| **Model Line** | XC3 ULTRA GAMING |
| **Model Tier** | Mid-tier (between base XC3 and premium FTW3) |
| **Memory** | 24GB GDDR6X (24576 MiB) |
| **Power Limit** | 420W |
| **Rated TDP** | 420W |
| **VBIOS** | 94.02.42.C0.05 |
| **CUDA Capability** | 8.6 |
| **Multiprocessors** | 82 |
| **PCI Bus ID** | 01:00.0 |

### PCI Identifiers

| ID Type | Value |
|---------|-------|
| **Vendor ID** | 10de (NVIDIA) |
| **Device ID** | 2204 (GA102 - RTX 3090 chip) |
| **Subsystem Vendor** | 3842 (EVGA) |
| **Subsystem Device** | 3982 (XC3 ULTRA model) |

---

## What This Means

### Not an FTW3

Your card is **NOT** an FTW3 model. Common confusion:
- ❌ **NOT** FTW3 Gaming (subsystem 3883, 420W)
- ❌ **NOT** FTW3 ULTRA Gaming (subsystem 3895/3897/3987, 450W)
- ✅ **IS** XC3 ULTRA Gaming (subsystem 3982, 420W)

### EVGA RTX 3090 Lineup

From lowest to highest tier:

1. **XC3 BLACK** (3881) - 350W, basic cooling
2. **XC3 GAMING** (3882) - 350W, standard cooling
3. **XC3 ULTRA** (3982) - **← YOUR MODEL** - 420W, enhanced cooling
4. **FTW3 GAMING** (3883) - 420W, premium cooling
5. **FTW3 ULTRA** (3895/3897/3987) - 450W, flagship cooling + highest overclock
6. **K|NGP|N HYBRID** (3971/3975) - 450W+, hybrid/water cooling, extreme

### XC3 ULTRA Features

**Cooling:**
- Triple-fan iCX3 cooling system
- Enhanced heatsink design
- ARGB lighting

**Power:**
- 420W TDP (same as FTW3 Gaming)
- Higher than base XC3 (350W)
- Lower than FTW3 ULTRA (450W)

**Performance:**
- Factory overclock above reference specs
- Good headroom for manual overclocking
- Positioned as "sweet spot" between price and performance

**Build Quality:**
- Premium PCB design
- Quality components
- EVGA's 3-year warranty (extendable)

---

## Identification Tools

### Automatic Tool

Created: [gpu_benchmarks/identify_gpu.py](gpu_benchmarks/identify_gpu.py)

**Usage:**
```bash
source venv/bin/activate

# Identify this GPU
python gpu_benchmarks/identify_gpu.py --gpu 0

# Save to JSON
python gpu_benchmarks/identify_gpu.py --gpu 0 --save

# Identify all GPUs
python gpu_benchmarks/identify_gpu.py --all
```

### Manual Commands

```bash
# Get basic info
nvidia-smi --query-gpu=name,memory.total,power.limit,vbios_version --format=csv,noheader -i 0

# Get subsystem ID (most important for model identification)
lspci -vnn -s 01:00.0 | grep -i subsystem

# Output shows: Subsystem: eVga.com. Corp. ... [3842:3982]
#               Vendor: 3842 (EVGA), Device: 3982 (XC3 ULTRA)
```

---

## Documentation

### Complete Guides

1. **[GPU_IDENTIFICATION_GUIDE.md](gpu_benchmarks/GPU_IDENTIFICATION_GUIDE.md)**
   - Complete agent instructions for GPU identification
   - Model database reference
   - Manual identification process
   - Troubleshooting guide

2. **[identify_gpu.py](gpu_benchmarks/identify_gpu.py)**
   - Automated identification tool
   - Supports EVGA, ASUS, Gigabyte, MSI, and more
   - JSON export capability
   - Multi-GPU support

### How to Use This Information

**When asking future questions about your GPU:**
- You can reference this file
- Or run: `python gpu_benchmarks/identify_gpu.py --gpu 0`
- Or ask to check the saved JSON file

**Saved Identification Files:**
- JSON format: `gpu_identification_GPU0_YYYYMMDD_HHMMSS.json`
- Contains complete specifications
- Includes timestamp for tracking

---

## Quick Reference

### Interactive Menu Access

Run: `./gpu_benchmarks/run_benchmark.sh`

**Menu Options (planned/updated):**
- Option 1: Identify GPU Model
- Options 2-4: Monitoring tools
- Options 5-8: Benchmarking
- Options 9-12: Stress testing
- Options 20-24: Multi-GPU testing

### Common Questions

**Q: Is this an FTW3?**
A: No, this is an XC3 ULTRA. FTW3 models have different subsystem IDs (3883, 3895, etc.)

**Q: What's the power limit?**
A: 420W (same as FTW3 Gaming, lower than FTW3 ULTRA's 450W)

**Q: Is this a good model?**
A: Yes, it's EVGA's mid-tier offering with excellent cooling and performance. Good balance between cost and capability.

**Q: Can I overclock it?**
A: Yes, the 420W power limit provides good headroom. It's already factory overclocked above reference.

**Q: How does it compare to FTW3?**
A: FTW3 has better binned chips, more premium cooling, and FTW3 ULTRA has 30W more power (450W). XC3 ULTRA is 90% of the performance for less cost.

---

## Agent Instructions for Future Sessions

When asked about this GPU in future conversations:

1. **Check this file first:** `GPU_IDENTIFICATION_SAVED.md`
2. **Or run:** `python gpu_benchmarks/identify_gpu.py --gpu 0`
3. **Or read JSON:** `gpu_identification_GPU0_*.json`

**Key points to remember:**
- Model: EVGA RTX 3090 XC3 ULTRA GAMING
- Subsystem ID: 3842:3982
- NOT an FTW3 model
- 420W power limit
- Mid-tier EVGA model

**Always clarify:**
- Exact variant when discussing specifications
- Power limits when discussing overclocking
- Cooling capabilities when discussing thermal performance

---

## Related Files

**Identification:**
- `gpu_benchmarks/identify_gpu.py` - Automated tool
- `gpu_benchmarks/GPU_IDENTIFICATION_GUIDE.md` - Complete guide
- `gpu_identification_GPU0_*.json` - Saved identifications

**Benchmarking:**
- `gpu_benchmarks/gpu_benchmark.py` - Performance testing
- `gpu_benchmarks/gpu_stress_test.py` - Stability testing
- `gpu_benchmarks/compare_results.py` - Multi-GPU comparison

**Documentation:**
- `MULTI_GPU_READY.md` - Multi-GPU enhancements
- `gpu_benchmarks/README.md` - Main documentation
- `gpu_benchmarks/QUICKSTART.md` - Quick reference

---

## Summary

✅ **Your GPU is positively identified as:**

**EVGA GeForce RTX 3090 XC3 ULTRA GAMING**

- Mid-tier EVGA model
- 420W TDP
- Triple-fan cooling
- 24GB GDDR6X memory
- Excellent performance and value
- Good overclockingtential

This information has been saved and can be retrieved anytime using the identification tools.
