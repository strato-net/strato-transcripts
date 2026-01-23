# GPU Identification Guide - Agent Instructions

## Purpose

This document provides comprehensive instructions for identifying exact GPU models, including manufacturer variants (EVGA FTW3, ASUS ROG Strix, etc.). Use this guide whenever you need to:
- Identify what exact GPU model is installed
- Differentiate between variants of the same GPU (e.g., RTX 3090 FTW3 vs XC3)
- Gather complete hardware specifications
- Save GPU identification for reference

---

## Quick Start

### For Users:

```bash
# Identify specific GPU
source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0

# Identify all GPUs
python gpu_benchmarks/identify_gpu.py --all

# Save identification to JSON
python gpu_benchmarks/identify_gpu.py --gpu 0 --save
```

### For AI Agents:

When asked "what exact model is my GPU?", follow these steps:

1. **Run the identification script:**
   ```bash
   source venv/bin/activate
   python gpu_benchmarks/identify_gpu.py --gpu 0
   ```

2. **If script not available, use manual commands:**
   ```bash
   # Get basic info
   nvidia-smi --query-gpu=name,memory.total,power.limit,vbios_version --format=csv

   # Get subsystem ID (most important for model identification)
   lspci -vnn -s $(nvidia-smi --query-gpu=pci.bus_id --format=csv,noheader -i 0 | cut -d: -f2-) | grep -i subsystem
   ```

3. **Interpret subsystem ID:**
   - Format: `[vendor:device]`
   - Example: `[3842:3982]`
   - `3842` = EVGA
   - `3982` = XC3 ULTRA model

4. **Provide clear answer with:**
   - Exact model name
   - Manufacturer
   - Model tier (Base/Mid/High/Flagship)
   - Power specifications
   - Key differentiators

---

## Tool: identify_gpu.py

### Location
```
gpu_benchmarks/identify_gpu.py
```

### Features

✅ **Automatic Model Detection**
- Identifies manufacturer (EVGA, ASUS, Gigabyte, MSI, etc.)
- Determines exact variant (FTW3, Strix, Gaming OC, etc.)
- Classifies model tier (Base, Mid, High, Flagship, Extreme)

✅ **Comprehensive Information**
- Hardware specs (memory, power, VBIOS)
- CUDA capabilities
- PCI identifiers
- Model classification

✅ **Multiple Output Formats**
- Formatted report (default)
- JSON output (`--json`)
- Save to file (`--save`)

✅ **Multi-GPU Support**
- Single GPU (`--gpu 0`)
- All GPUs (`--all`)

### Usage Examples

```bash
# Basic identification
python identify_gpu.py --gpu 0

# Identify all GPUs
python identify_gpu.py --all

# Save to JSON file
python identify_gpu.py --gpu 0 --save

# Output as JSON only
python identify_gpu.py --gpu 0 --json

# Identify all and save
python identify_gpu.py --all --save
```

### Sample Output

```
================================================================================
GPU 0 IDENTIFICATION REPORT
================================================================================

BASIC INFORMATION:
  GPU Name:          NVIDIA GeForce RTX 3090
  Manufacturer:      EVGA
  Model:             EVGA RTX 3090 XC3 ULTRA GAMING
  Model Tier:        Mid

HARDWARE DETAILS:
  Memory:            24576 MiB
  Power Limit:       420.0 W
  Rated TDP:         420 W
  VBIOS Version:     94.02.42.C0.05
  PCI Bus ID:        01:00.0

CUDA INFORMATION:
  CUDA Capability:   8.6
  Multiprocessors:   82
  Total Memory:      23.55 GB

PCI IDENTIFIERS:
  Vendor ID:         10de
  Device ID:         2204
  Subsystem Vendor:  3842
  Subsystem Device:  3982

MODEL CLASSIFICATION:
  Tier:              Mid
  Description:       Mid-tier model with enhanced cooling and mild overclock
```

---

## Understanding GPU Model Identification

### Why Model Identification Matters

Different variants of the same GPU chip can have:
- **Different cooling solutions** (air vs hybrid vs water)
- **Different power limits** (350W vs 420W vs 450W)
- **Different factory overclocks** (boost clocks)
- **Different build quality** (components, PCB layers)
- **Different warranties** (3-year vs 5-year)
- **Different prices** (can vary by $200+)

Example: RTX 3090 comes in these EVGA variants:
- **XC3 BLACK** - 350W, basic cooling
- **XC3 ULTRA** - 420W, enhanced cooling
- **FTW3 GAMING** - 420W, premium cooling
- **FTW3 ULTRA** - 450W, best cooling + highest overclock
- **K|NGP|N** - 450W+, hybrid cooling, extreme overclock

### Key Identifiers

#### 1. Subsystem ID (Most Important)

Format: `[vendor:device]`

**Common Vendors:**
- `3842` = EVGA
- `1043` = ASUS
- `1458` = Gigabyte
- `1462` = MSI
- `10DE` = NVIDIA (Founders Edition)
- `196E` = PNY
- `19DA` = Zotac
- `1569` = Palit

**Device ID:** Identifies specific model variant
- For EVGA RTX 3090:
  - `3881` = XC3 BLACK
  - `3982` = XC3 ULTRA
  - `3883` = FTW3 GAMING
  - `3895`/`3897`/`3987` = FTW3 ULTRA

#### 2. Power Limit

Indicates model tier:
- **350W** = Reference/Base models
- **370-390W** = Mid-tier models
- **420W** = High-end models
- **450W+** = Flagship/Extreme models

#### 3. VBIOS Version

Manufacturer-specific versioning:
- EVGA format: `94.02.42.C0.05`
- ASUS format: Similar but different numbering
- Can indicate BIOS updates or revisions

---

## Model Database Reference

### EVGA RTX 3090 Models

| Subsystem ID | Model Name | Power | Tier | Cooling |
|--------------|------------|-------|------|---------|
| 3881 | XC3 BLACK GAMING | 350W | Base | Triple-fan |
| 3882 | XC3 GAMING | 350W | Base | Triple-fan |
| 3982 | **XC3 ULTRA GAMING** | 420W | Mid | Triple-fan |
| 3883 | FTW3 GAMING | 420W | High | Triple-fan+ |
| 3895/3897/3987 | FTW3 ULTRA GAMING | 450W | Flagship | Triple-fan++ |
| 3971/3975 | K\|NGP\|N HYBRID | 450W+ | Extreme | Hybrid |

### ASUS RTX 3090 Models

| Subsystem ID | Model Name | Power | Tier |
|--------------|------------|-------|------|
| 87E2 | TUF GAMING OC | 375W | Mid |
| 87E3 | ROG STRIX OC | 420W | High |

### Gigabyte RTX 3090 Models

| Subsystem ID | Model Name | Power | Tier |
|--------------|------------|-------|------|
| 403C | GAMING OC | 370W | Mid |
| 403E | AORUS MASTER | 420W | High |

### MSI RTX 3090 Models

| Subsystem ID | Model Name | Power | Tier |
|--------------|------------|-------|------|
| 38A2 | GAMING X TRIO | 370W | Mid |
| 38A1 | SUPRIM X | 420W | High |

---

## Agent Instructions - Step-by-Step

### Scenario 1: User Asks "What exact model is my GPU?"

**Step 1: Run identification script**
```bash
source venv/bin/activate
python gpu_benchmarks/identify_gpu.py --gpu 0
```

**Step 2: Parse output and identify key information**
- Manufacturer (EVGA, ASUS, etc.)
- Model name (XC3 ULTRA, FTW3, etc.)
- Model tier (Base, Mid, High, Flagship)
- Power specifications

**Step 3: Provide clear, concise answer**

Example response:
```
Your GPU is: EVGA GeForce RTX 3090 XC3 ULTRA GAMING

Key Details:
- Manufacturer: EVGA
- Model Tier: Mid-tier (between XC3 and FTW3)
- Power Limit: 420W
- Cooling: Triple-fan XC3 design

This is NOT an FTW3 model. The XC3 ULTRA sits between the base XC3
and the premium FTW3 series. It has better cooling than base XC3 but
less power headroom than FTW3 ULTRA (450W).
```

**Step 4: Offer to save identification**
```
Would you like me to save this identification to a file for future reference?
```

---

### Scenario 2: User Has Multiple GPUs

**Step 1: Identify all GPUs**
```bash
python gpu_benchmarks/identify_gpu.py --all
```

**Step 2: Summarize all GPUs**
```
You have 4 GPUs installed:

GPU 0: EVGA RTX 3090 XC3 ULTRA GAMING (420W, Mid-tier)
GPU 1: EVGA RTX 4090 FTW3 ULTRA GAMING (600W, Flagship)
GPU 2: ASUS RTX 3080 TUF GAMING OC (375W, Mid-tier)
GPU 3: MSI RTX 3070 GAMING X TRIO (290W, Mid-tier)
```

**Step 3: Offer detailed report if needed**

---

### Scenario 3: Script Not Available

**Step 1: Gather information manually**

```bash
# Basic info
nvidia-smi --query-gpu=name,memory.total,power.limit --format=csv,noheader -i 0

# Get PCI bus ID
nvidia-smi --query-gpu=pci.bus_id --format=csv,noheader -i 0

# Get subsystem ID (use bus ID from above, removing leading 0000:)
lspci -vnn -s 01:00.0 | grep -i subsystem
```

**Step 2: Parse subsystem ID**
```
Output: Subsystem: eVga.com. Corp. GA102 [GeForce RTX 3090] [3842:3982]
                                                               ^^^^^
                                                               Vendor:Device
```

**Step 3: Look up in database**
- Vendor: 3842 = EVGA
- Device: 3982 = XC3 ULTRA GAMING (refer to table above)

**Step 4: Provide answer**

---

### Scenario 4: Unknown Model

**If subsystem ID not in database:**

**Step 1: Provide available information**
```
Your GPU is an NVIDIA GeForce RTX 3090, but the specific manufacturer
variant could not be determined from the database.

Subsystem ID: [vendor:device]
Manufacturer: [Based on vendor ID]
Power Limit: [from nvidia-smi]
```

**Step 2: Offer to research**
```
I can search online for this specific subsystem ID to identify the
exact model, or we can add it to the database for future reference.
```

**Step 3: Update database if confirmed**
After confirming the model, update `identify_gpu.py` with new entry.

---

## Manual Identification Process

If automated tools are unavailable, follow this manual process:

### 1. Get Basic GPU Info
```bash
nvidia-smi
```
Look for: Name, Memory, Power Draw

### 2. Get Subsystem ID
```bash
# Method 1: Using nvidia-smi and lspci
nvidia-smi --query-gpu=pci.bus_id --format=csv,noheader -i 0
lspci -vnn -s [bus_id] | grep -i subsystem

# Method 2: Direct lspci (if you know the bus ID)
lspci -vnn | grep -A 1 "VGA.*3090"
```

### 3. Get VBIOS Version
```bash
nvidia-smi --query-gpu=vbios_version --format=csv,noheader -i 0
```

### 4. Get Power Limit
```bash
nvidia-smi --query-gpu=power.limit --format=csv,noheader -i 0
```

### 5. Cross-Reference with Database
Use the subsystem ID to look up the exact model in the tables above.

---

## Extending the Database

To add new GPU models to the identification database:

### 1. Identify New Model

Gather:
- Subsystem vendor ID
- Subsystem device ID
- Model name
- Power specifications
- Model tier

### 2. Update identify_gpu.py

Add entry to appropriate manufacturer dictionary:

```python
EVGA_RTX_3090_MODELS = {
    # Existing entries...
    "XXXX": {"name": "Model Name", "power": 420, "tier": "High"},
}
```

### 3. Test

```bash
python identify_gpu.py --gpu 0
```

Verify the new model is correctly identified.

---

## Troubleshooting

### Issue: Script Can't Find GPU

**Solution:**
```bash
# Verify GPU is visible
nvidia-smi

# Check PyTorch can see it
python -c "import torch; print(torch.cuda.device_count())"

# Run with specific GPU ID
python identify_gpu.py --gpu 0
```

### Issue: Subsystem ID Not Recognized

**Solution:**
- Manually look up the subsystem ID online
- Search: "subsystem id [vendor:device] GPU"
- Add to database in `identify_gpu.py`

### Issue: Permission Denied for lspci

**Solution:**
```bash
# Most lspci commands don't need sudo
lspci -vnn -s 01:00.0

# If needed, try without extended info
lspci -nn | grep VGA
```

### Issue: Wrong Model Detected

**Verification steps:**
1. Check power limit matches expected model
2. Verify VBIOS version
3. Cross-reference with manufacturer's website
4. Check serial number (if available)

---

## Integration with Benchmarking Suite

### Save Identification Before Benchmarking

```bash
# Good practice: Identify GPU before benchmarking
python gpu_benchmarks/identify_gpu.py --gpu 0 --save

# Then run benchmarks
python gpu_benchmarks/gpu_benchmark.py --gpu 0 --save
```

### Include in Results

When creating benchmark reports, include GPU identification:
- Exact model name
- Manufacturer
- Model tier
- Power specifications

This helps when comparing results across different GPU variants.

---

## Quick Reference Commands

```bash
# Identify specific GPU
python gpu_benchmarks/identify_gpu.py --gpu 0

# Identify all GPUs
python gpu_benchmarks/identify_gpu.py --all

# Save to JSON
python gpu_benchmarks/identify_gpu.py --gpu 0 --save

# Get just JSON output
python gpu_benchmarks/identify_gpu.py --gpu 0 --json

# Manual subsystem ID lookup
lspci -vnn | grep -A 1 "VGA.*NVIDIA"

# Get all GPU power limits
nvidia-smi --query-gpu=name,power.limit --format=csv
```

---

## Current System Identification

Based on last identification:

**GPU 0:**
- **Model:** EVGA GeForce RTX 3090 XC3 ULTRA GAMING
- **Subsystem ID:** 3842:3982
- **Power Limit:** 420W
- **Tier:** Mid-tier
- **VBIOS:** 94.02.42.C0.05

This is NOT an FTW3 model. The XC3 ULTRA is EVGA's mid-tier RTX 3090,
positioned between the base XC3 (350W) and the flagship FTW3 ULTRA (450W).

---

## Notes for Future Reference

- Always run identification before major benchmarking sessions
- Save identification files for historical tracking
- Update database when encountering new models
- Cross-reference power limit with model specifications
- VBIOS version can change with updates (note original version)

---

## See Also

- [MULTI_GPU_GUIDE.md](MULTI_GPU_GUIDE.md) - Multi-GPU testing
- [README.md](README.md) - Main benchmarking documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick reference guide
