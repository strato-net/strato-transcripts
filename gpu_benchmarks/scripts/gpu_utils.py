#!/usr/bin/env python3
"""
GPU Utilities - Unified support for NVIDIA and AMD GPUs
Provides vendor-agnostic GPU detection, monitoring, and identification
"""
import subprocess
import re
import os
import shutil
from enum import Enum
from typing import Optional, Dict, Any, List

class GPUVendor(Enum):
    NVIDIA = "nvidia"
    AMD = "amd"
    UNKNOWN = "unknown"

def detect_gpu_vendor() -> GPUVendor:
    """Detect which GPU vendor is present in the system"""
    # Check for NVIDIA
    if shutil.which('nvidia-smi'):
        try:
            result = subprocess.run(['nvidia-smi', '-L'], capture_output=True, text=True)
            if result.returncode == 0 and 'NVIDIA' in result.stdout:
                return GPUVendor.NVIDIA
        except:
            pass

    # Check for AMD
    if shutil.which('rocm-smi'):
        try:
            result = subprocess.run(['rocm-smi', '-i'], capture_output=True, text=True)
            if result.returncode == 0:
                return GPUVendor.AMD
        except:
            pass

    # Also check via lspci
    try:
        result = subprocess.run(['lspci'], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.upper()
            if 'NVIDIA' in output:
                return GPUVendor.NVIDIA
            elif 'AMD' in output or 'ATI' in output or 'RADEON' in output:
                return GPUVendor.AMD
    except:
        pass

    return GPUVendor.UNKNOWN

def get_gpu_count(vendor: GPUVendor = None) -> int:
    """Get the number of GPUs available"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=count', '--format=csv,noheader,nounits'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return int(result.stdout.strip().split('\n')[0])
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            result = subprocess.run(['rocm-smi', '-i'], capture_output=True, text=True)
            if result.returncode == 0:
                # Count GPU entries
                gpu_count = len(re.findall(r'GPU\[(\d+)\]', result.stdout))
                return max(1, gpu_count)
        except:
            pass

    # Fallback to PyTorch
    try:
        import torch
        if torch.cuda.is_available():
            return torch.cuda.device_count()
    except:
        pass

    return 0

def get_gpu_temperature(gpu_id: int = 0, vendor: GPUVendor = None) -> Optional[int]:
    """Get GPU temperature in Celsius"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader,nounits', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return int(result.stdout.strip())
        except:
            pass

        # Try PyTorch method
        try:
            import torch
            return torch.cuda.temperature(gpu_id)
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-t'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                # Parse temperature from output
                temp_match = re.search(r'Temperature.*?:\s*(\d+)', result.stdout)
                if temp_match:
                    return int(temp_match.group(1))
        except:
            pass

    return None

def get_gpu_power(gpu_id: int = 0, vendor: GPUVendor = None) -> Optional[float]:
    """Get GPU power draw in Watts"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=power.draw', '--format=csv,noheader,nounits', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return float(result.stdout.strip())
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-P'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                # Parse power from output
                power_match = re.search(r'Average.*?:\s*([\d.]+)', result.stdout)
                if power_match:
                    return float(power_match.group(1))
        except:
            pass

    return None

def get_gpu_utilization(gpu_id: int = 0, vendor: GPUVendor = None) -> Optional[int]:
    """Get GPU utilization percentage"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return int(result.stdout.strip())
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-u'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                # Parse utilization from output
                util_match = re.search(r'GPU use.*?:\s*(\d+)', result.stdout)
                if util_match:
                    return int(util_match.group(1))
        except:
            pass

    return None

def get_gpu_memory_info(gpu_id: int = 0, vendor: GPUVendor = None) -> Dict[str, float]:
    """Get GPU memory info (total, used, free) in GB"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    info = {'total': 0, 'used': 0, 'free': 0}

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=memory.total,memory.used,memory.free',
                 '--format=csv,noheader,nounits', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                parts = result.stdout.strip().split(', ')
                info['total'] = float(parts[0]) / 1024  # Convert MiB to GB
                info['used'] = float(parts[1]) / 1024
                info['free'] = float(parts[2]) / 1024
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '--showmeminfo', 'vram'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                total_match = re.search(r'Total.*?:\s*(\d+)', result.stdout)
                used_match = re.search(r'Used.*?:\s*(\d+)', result.stdout)
                if total_match:
                    info['total'] = int(total_match.group(1)) / 1024 / 1024 / 1024
                if used_match:
                    info['used'] = int(used_match.group(1)) / 1024 / 1024 / 1024
                info['free'] = info['total'] - info['used']
        except:
            pass

    return info

def get_gpu_clocks(gpu_id: int = 0, vendor: GPUVendor = None) -> Dict[str, int]:
    """Get GPU clock speeds in MHz"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    clocks = {'graphics': 0, 'memory': 0}

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=clocks.current.graphics,clocks.current.memory',
                 '--format=csv,noheader,nounits', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                parts = result.stdout.strip().split(', ')
                clocks['graphics'] = int(parts[0])
                clocks['memory'] = int(parts[1])
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-c'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                sclk_match = re.search(r'sclk.*?:\s*(\d+)', result.stdout, re.IGNORECASE)
                mclk_match = re.search(r'mclk.*?:\s*(\d+)', result.stdout, re.IGNORECASE)
                if sclk_match:
                    clocks['graphics'] = int(sclk_match.group(1))
                if mclk_match:
                    clocks['memory'] = int(mclk_match.group(1))
        except:
            pass

    return clocks

def get_basic_gpu_info(gpu_id: int = 0, vendor: GPUVendor = None) -> Dict[str, Any]:
    """Get basic GPU information"""
    if vendor is None:
        vendor = detect_gpu_vendor()

    info = {
        'vendor': vendor.value,
        'id': gpu_id,
        'name': 'Unknown',
        'memory_total': 0,
        'power_limit': 0,
        'bus_id': '',
        'vbios': '',
    }

    if vendor == GPUVendor.NVIDIA:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=name,memory.total,power.limit,gpu_bus_id,vbios_version',
                 '--format=csv,noheader', '-i', str(gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                parts = result.stdout.strip().split(', ')
                info['name'] = parts[0]
                info['memory_total'] = parts[1]
                info['power_limit'] = float(parts[2].replace(' W', ''))
                info['bus_id'] = parts[3].replace('0000:', '')
                info['vbios'] = parts[4]
        except:
            pass

    elif vendor == GPUVendor.AMD:
        try:
            # Get GPU name
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-i'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                # Parse device info
                card_match = re.search(r'Card series:\s*(.+)', result.stdout)
                if card_match:
                    info['name'] = card_match.group(1).strip()

                # Get VRAM
                vram_match = re.search(r'VRAM Total Memory.*?:\s*(\d+)', result.stdout)
                if vram_match:
                    info['memory_total'] = f"{int(vram_match.group(1)) // (1024*1024)} MiB"

            # Get power limit
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-P'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                power_match = re.search(r'Max.*?:\s*([\d.]+)', result.stdout)
                if power_match:
                    info['power_limit'] = float(power_match.group(1))

            # Get VBIOS
            result = subprocess.run(
                ['rocm-smi', '-d', str(gpu_id), '-v'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                vbios_match = re.search(r'VBIOS.*?:\s*(.+)', result.stdout)
                if vbios_match:
                    info['vbios'] = vbios_match.group(1).strip()
        except:
            pass

    return info

def get_pci_info(bus_id: str = "01:00.0") -> Dict[str, str]:
    """Get PCI subsystem information for a GPU"""
    info = {
        'vendor_id': '',
        'device_id': '',
        'subsystem_vendor_id': '',
        'subsystem_device_id': '',
        'manufacturer': '',
    }

    try:
        result = subprocess.run(
            ['lspci', '-vnn', '-s', bus_id],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            output = result.stdout

            # Extract vendor and device IDs
            vendor_match = re.search(r'\[([0-9a-fA-F]{4}):([0-9a-fA-F]{4})\]', output)
            if vendor_match:
                info['vendor_id'] = vendor_match.group(1)
                info['device_id'] = vendor_match.group(2)

            # Extract subsystem vendor and device IDs
            subsys_match = re.search(r'Subsystem:.*?\[([0-9a-fA-F]{4}):([0-9a-fA-F]{4})\]', output)
            if subsys_match:
                info['subsystem_vendor_id'] = subsys_match.group(1)
                info['subsystem_device_id'] = subsys_match.group(2)

            # Extract manufacturer name
            subsys_name_match = re.search(r'Subsystem: (.*?) \[', output)
            if subsys_name_match:
                info['manufacturer'] = subsys_name_match.group(1).strip()
    except:
        pass

    return info

def check_pytorch_backend() -> str:
    """Check which PyTorch backend is available"""
    try:
        import torch
        if torch.cuda.is_available():
            # Check if it's ROCm or CUDA
            if hasattr(torch.version, 'hip') and torch.version.hip is not None:
                return f"ROCm {torch.version.hip}"
            elif torch.version.cuda is not None:
                return f"CUDA {torch.version.cuda}"
            else:
                return "CUDA (version unknown)"
        else:
            return "CPU only (no GPU backend)"
    except ImportError:
        return "PyTorch not installed"

def print_system_info():
    """Print system GPU information"""
    vendor = detect_gpu_vendor()
    gpu_count = get_gpu_count(vendor)
    backend = check_pytorch_backend()

    print("=" * 60)
    print("GPU SYSTEM INFORMATION")
    print("=" * 60)
    print(f"GPU Vendor:     {vendor.value.upper()}")
    print(f"GPU Count:      {gpu_count}")
    print(f"PyTorch Backend: {backend}")
    print()

    for i in range(gpu_count):
        info = get_basic_gpu_info(i, vendor)
        print(f"GPU {i}: {info['name']}")
        print(f"  Memory: {info['memory_total']}")
        print(f"  Power Limit: {info['power_limit']}W")
        if info['vbios']:
            print(f"  VBIOS: {info['vbios']}")
        print()

    print("=" * 60)

# ============================================================================
# AMD GPU Model Databases (for identification)
# ============================================================================

# Sapphire (1DA2)
SAPPHIRE_GPU_MODELS = {
    # RX 7900 XTX
    "E471": {"name": "RX 7900 XTX NITRO+", "power": 420, "tier": "Flagship"},
    "E472": {"name": "RX 7900 XTX PURE", "power": 355, "tier": "Mid"},
    # RX 7900 XT
    "E475": {"name": "RX 7900 XT NITRO+", "power": 391, "tier": "High"},
    # RX 7800 XT
    "E478": {"name": "RX 7800 XT NITRO+", "power": 263, "tier": "High"},
    # RX 7600
    "E481": {"name": "RX 7600 PULSE", "power": 165, "tier": "Mid"},
    # RX 6900 XT
    "E439": {"name": "RX 6900 XT NITRO+ SE", "power": 303, "tier": "Flagship"},
    # RX 6800 XT
    "E438": {"name": "RX 6800 XT NITRO+ SE", "power": 300, "tier": "High"},
    "E43B": {"name": "RX 6800 XT NITRO+", "power": 300, "tier": "High"},
}

# XFX (1682)
XFX_GPU_MODELS = {
    # RX 7900 XTX
    "5707": {"name": "RX 7900 XTX SPEEDSTER MERC 310", "power": 420, "tier": "Flagship"},
    # RX 7900 XT
    "5706": {"name": "RX 7900 XT SPEEDSTER MERC 310", "power": 391, "tier": "High"},
    # RX 6900 XT
    "D190": {"name": "RX 6900 XT SPEEDSTER MERC 319", "power": 330, "tier": "Flagship"},
    # RX 6800 XT
    "D191": {"name": "RX 6800 XT SPEEDSTER MERC 319", "power": 300, "tier": "High"},
}

# PowerColor (148C)
POWERCOLOR_GPU_MODELS = {
    # RX 7900 XTX
    "2420": {"name": "RX 7900 XTX RED DEVIL", "power": 420, "tier": "Flagship"},
    "2421": {"name": "RX 7900 XTX HELLHOUND", "power": 355, "tier": "Mid"},
    # RX 7900 XT
    "2422": {"name": "RX 7900 XT RED DEVIL", "power": 391, "tier": "High"},
    # RX 6900 XT
    "2410": {"name": "RX 6900 XT RED DEVIL", "power": 330, "tier": "Flagship"},
    "2411": {"name": "RX 6900 XT RED DEVIL ULTIMATE", "power": 330, "tier": "Extreme"},
}

# ASUS (1043) - AMD cards
ASUS_AMD_GPU_MODELS = {
    # RX 7900 XTX
    "88E0": {"name": "RX 7900 XTX TUF GAMING OC", "power": 390, "tier": "Mid"},
    "88E1": {"name": "RX 7900 XTX ROG STRIX OC", "power": 420, "tier": "Flagship"},
    # RX 7900 XT
    "88E4": {"name": "RX 7900 XT TUF GAMING OC", "power": 345, "tier": "Mid"},
    # RX 6900 XT
    "04E0": {"name": "RX 6900 XT TUF GAMING OC", "power": 303, "tier": "Mid"},
    "04E1": {"name": "RX 6900 XT ROG STRIX LC OC", "power": 330, "tier": "Flagship"},
}

# Gigabyte (1458) - AMD cards
GIGABYTE_AMD_GPU_MODELS = {
    # RX 7900 XTX
    "1001": {"name": "RX 7900 XTX GAMING OC", "power": 420, "tier": "High"},
    # RX 7900 XT
    "1002": {"name": "RX 7900 XT GAMING OC", "power": 391, "tier": "High"},
    # RX 6900 XT
    "2330": {"name": "RX 6900 XT AORUS MASTER", "power": 330, "tier": "Flagship"},
}

# MSI (1462) - AMD cards
MSI_AMD_GPU_MODELS = {
    # RX 7900 XTX
    "3974": {"name": "RX 7900 XTX GAMING TRIO CLASSIC", "power": 420, "tier": "High"},
    # RX 7900 XT
    "3975": {"name": "RX 7900 XT GAMING TRIO CLASSIC", "power": 391, "tier": "High"},
    # RX 6900 XT
    "9502": {"name": "RX 6900 XT GAMING X TRIO", "power": 303, "tier": "High"},
}

# AMD Reference (1002)
AMD_REFERENCE_MODELS = {
    # RX 7000 series
    "744C": {"name": "RX 7900 XTX", "power": 355, "tier": "Reference"},
    "744E": {"name": "RX 7900 XT", "power": 315, "tier": "Reference"},
    "7480": {"name": "RX 7800 XT", "power": 263, "tier": "Reference"},
    "7481": {"name": "RX 7700 XT", "power": 245, "tier": "Reference"},
    # RX 6000 series
    "73BF": {"name": "RX 6900 XT", "power": 300, "tier": "Reference"},
    "73AF": {"name": "RX 6800 XT", "power": 300, "tier": "Reference"},
    "73A5": {"name": "RX 6800", "power": 250, "tier": "Reference"},
}

def identify_amd_model(subsystem_vendor: str, subsystem_device: str, device_id: str = "") -> Dict[str, Any]:
    """Identify AMD GPU model from subsystem IDs"""
    subsys_vendor = subsystem_vendor.upper()
    subsys_device = subsystem_device.upper()

    model_info = None
    manufacturer = "Unknown"

    # Sapphire (1DA2)
    if subsys_vendor == '1DA2':
        model_info = SAPPHIRE_GPU_MODELS.get(subsys_device)
        manufacturer = "Sapphire"

    # XFX (1682)
    elif subsys_vendor == '1682':
        model_info = XFX_GPU_MODELS.get(subsys_device)
        manufacturer = "XFX"

    # PowerColor (148C)
    elif subsys_vendor == '148C':
        model_info = POWERCOLOR_GPU_MODELS.get(subsys_device)
        manufacturer = "PowerColor"

    # ASUS (1043)
    elif subsys_vendor == '1043':
        model_info = ASUS_AMD_GPU_MODELS.get(subsys_device)
        manufacturer = "ASUS"

    # Gigabyte (1458)
    elif subsys_vendor == '1458':
        model_info = GIGABYTE_AMD_GPU_MODELS.get(subsys_device)
        manufacturer = "Gigabyte"

    # MSI (1462)
    elif subsys_vendor == '1462':
        model_info = MSI_AMD_GPU_MODELS.get(subsys_device)
        manufacturer = "MSI"

    # AMD Reference (1002)
    elif subsys_vendor == '1002':
        model_info = AMD_REFERENCE_MODELS.get(device_id.upper())
        manufacturer = "AMD"

    if model_info:
        return {
            'manufacturer': manufacturer,
            'model_name': f"{manufacturer} {model_info['name']}",
            'model_tier': model_info['tier'],
            'rated_power': model_info['power'],
        }
    else:
        return {
            'manufacturer': manufacturer,
            'model_name': f"Unknown AMD variant (Subsystem: {subsys_vendor}:{subsys_device})",
            'model_tier': 'Unknown',
            'rated_power': None,
        }

if __name__ == "__main__":
    print_system_info()
