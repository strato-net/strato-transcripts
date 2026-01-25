# GPU Installation and Benchmarking

This skill covers installing GPU drivers (NVIDIA, AMD, Intel) on Ubuntu, setting up Python environments for WhisperX transcription, and running PyTorch benchmarks.

## Quick Start

### 1. Install GPU Drivers
```bash
sudo ./scripts/install_nvidia_drivers.sh && sudo reboot  # NVIDIA
sudo ./scripts/install_amd_drivers.sh && sudo reboot     # AMD
sudo ./scripts/install_intel_drivers.sh && sudo reboot   # Intel
```

### 2. Create Python Environments
```bash
./scripts/install_packages_and_venv.sh --nvidia   # NVIDIA venv
./scripts/install_packages_and_venv.sh --amd      # AMD venv
./scripts/install_packages_and_venv.sh --intel    # Intel venv
./scripts/install_packages_and_venv.sh --cpu      # CPU-only venv
./scripts/install_packages_and_venv.sh --all      # All four venvs
```

### 3. Activate Based on Connected GPU
```bash
source setup_env.sh
source venv-nvidia/bin/activate   # NVIDIA eGPU connected
source venv-amd/bin/activate      # AMD eGPU connected
source venv-intel/bin/activate    # Intel iGPU fallback
source venv-cpu/bin/activate      # CPU-only fallback
```

---

## Python Virtual Environments

Each venv contains WhisperX with all patches and the correct PyTorch backend:

| venv | Backend | PyTorch Version | Use Case |
|------|---------|-----------------|----------|
| `venv-nvidia/` | CUDA | 2.9.1+cu130 | NVIDIA discrete/eGPU |
| `venv-amd/` | ROCm | 2.6.0+rocm6.2 | AMD discrete/eGPU |
| `venv-intel/` | XPU (IPEX) | 2.5.1 + IPEX 2.5.10 | Intel integrated/Arc |
| `venv-cpu/` | CPU | 2.9.1 | Fallback, any system |

**eGPU Workflow:** Pre-create all venvs with `--all`, then activate the matching one based on which GPU is currently connected.

---

## Driver Installation

### NVIDIA
```bash
sudo apt update && sudo apt upgrade -y
sudo ubuntu-drivers install
sudo reboot
# Verify: nvidia-smi
```

### AMD ROCm
```bash
# Add repository
sudo mkdir -p /etc/apt/keyrings
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo gpg --dearmor > /etc/apt/keyrings/rocm.gpg
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/latest $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update

# Install
sudo apt install -y amdgpu-dkms rocm-dev rocm-libs
sudo usermod -aG video,render $USER
sudo reboot
# Verify: rocminfo, rocm-smi
```

**Unofficial GPU Support (RX 6600/6700/6750 XT):**
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0
```

**Secure Boot Issues:** If amdgpu fails with "Key was rejected", enroll MOK at boot.

### Intel XPU
```bash
# Add repository
sudo mkdir -p /etc/apt/keyrings
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | sudo gpg --dearmor > /etc/apt/keyrings/intel-graphics.gpg
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu noble unified" | sudo tee /etc/apt/sources.list.d/intel-gpu.list
sudo apt update

# Install
sudo apt install -y level-zero intel-opencl-icd libze-intel-gpu1
sudo apt install -y intel-oneapi-runtime-dpcpp-cpp intel-oneapi-runtime-mkl
sudo usermod -aG video,render $USER
sudo reboot
# Verify: clinfo -l
```

**Package Note:** Use `libze-intel-gpu1` (not `intel-level-zero-gpu`) when `intel-opencl-icd` is installed.

---

## Benchmarking

### Benchmark Scripts
- `gpu_benchmarks/scripts/gpu_benchmark.py` - NVIDIA/AMD (CUDA/ROCm)
- `gpu_benchmarks/scripts/gpu_benchmark_intel.py` - Intel XPU

### Run Benchmarks

**NVIDIA:**
```bash
source venv-nvidia/bin/activate
cd gpu_benchmarks/scripts && python gpu_benchmark.py --save
```

**AMD:**
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0  # for unofficial GPUs
source venv-amd/bin/activate
cd gpu_benchmarks/scripts && python gpu_benchmark.py --save
```

**Intel:**
```bash
source venv-intel/bin/activate
cd gpu_benchmarks/scripts && python gpu_benchmark_intel.py --save
```

### Graphics Benchmarks (OpenGL/Vulkan)
```bash
DRI_PRIME=1 glmark2   # discrete/eGPU
DRI_PRIME=1 vkmark    # discrete/eGPU
glmark2               # integrated GPU
vkmark                # integrated GPU
```

### Results
- Individual JSON: `gpu_benchmarks/results/benchmark_*.json`
- Summary: `gpu_benchmarks/results/comparison_all_cards.json`

---

## eGPU Notes

- Thunderbolt 3/4 enclosures (e.g., Razer Core X) work on Linux
- Check detection: `lspci | grep -i vga`
- Use `DRI_PRIME=1` to run apps on eGPU
- Pre-create all venvs so you can switch based on connected GPU

---

## Troubleshooting

### GPU Not Detected
```bash
lspci | grep -i "vga\|3d\|display"
ls -la /dev/dri/
```

### Permission Denied on /dev/dri
```bash
sudo usermod -aG video,render $USER
# Logout/login or reboot
```

### ROCm "invalid device function"
```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0
```

### Intel XPU Shows False
1. Ensure `libze-intel-gpu1` is installed (not `intel-level-zero-gpu`)
2. Check user is in render group
3. Reboot after package installation

### Check Installed Packages
```bash
dpkg -l | grep nvidia                              # NVIDIA
dpkg -l | grep -E "rocm|amdgpu"                    # AMD
dpkg -l | grep -E "level-zero|intel-opencl|libze"  # Intel
```
