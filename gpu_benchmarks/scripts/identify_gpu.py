#!/usr/bin/env python3
"""
GPU Model Identification Tool
Identifies exact GPU model including manufacturer variant (EVGA FTW3, ASUS ROG, etc.)
Supports both NVIDIA and AMD GPUs
"""
import subprocess
import re
import json
from datetime import datetime

# Import unified GPU utilities
try:
    from gpu_utils import (
        GPUVendor, detect_gpu_vendor, get_gpu_count, get_basic_gpu_info,
        get_pci_info, identify_amd_model, get_gpu_temperature, get_gpu_power
    )
    HAS_GPU_UTILS = True
except ImportError:
    HAS_GPU_UTILS = False

# EVGA RTX 3090 Model Database
EVGA_RTX_3090_MODELS = {
    "3881": {"name": "RTX 3090 XC3 BLACK GAMING", "power": 350, "tier": "Base"},
    "3882": {"name": "RTX 3090 XC3 GAMING", "power": 350, "tier": "Base"},
    "3982": {"name": "RTX 3090 XC3 ULTRA GAMING", "power": 420, "tier": "Mid"},
    "3883": {"name": "RTX 3090 FTW3 GAMING", "power": 420, "tier": "High"},
    "3895": {"name": "RTX 3090 FTW3 ULTRA GAMING", "power": 450, "tier": "Flagship"},
    "3897": {"name": "RTX 3090 FTW3 ULTRA GAMING", "power": 450, "tier": "Flagship"},
    "3987": {"name": "RTX 3090 FTW3 ULTRA GAMING", "power": 450, "tier": "Flagship"},
    "3971": {"name": "RTX 3090 K|NGP|N HYBRID", "power": 450, "tier": "Extreme"},
    "3975": {"name": "RTX 3090 K|NGP|N HYBRID", "power": 450, "tier": "Extreme"},
}

# Other manufacturer databases (expandable)
ASUS_RTX_3090_MODELS = {
    "87E2": {"name": "RTX 3090 TUF GAMING OC", "power": 375, "tier": "Mid"},
    "87E3": {"name": "RTX 3090 ROG STRIX OC", "power": 420, "tier": "High"},
}

GIGABYTE_RTX_3090_MODELS = {
    "403C": {"name": "RTX 3090 GAMING OC", "power": 370, "tier": "Mid"},
    "403E": {"name": "RTX 3090 AORUS MASTER", "power": 420, "tier": "High"},
}

MSI_RTX_3090_MODELS = {
    "38A2": {"name": "RTX 3090 GAMING X TRIO", "power": 370, "tier": "Mid"},
    "38A1": {"name": "RTX 3090 SUPRIM X", "power": 420, "tier": "High"},
}

class GPUIdentifier:
    def __init__(self, gpu_id=0):
        self.gpu_id = gpu_id
        self.info = {}

        # Detect GPU vendor
        if HAS_GPU_UTILS:
            self.vendor = detect_gpu_vendor()
        else:
            # Fallback detection
            self.vendor = self._detect_vendor_fallback()

        self.info['vendor'] = self.vendor.value if HAS_GPU_UTILS else self.vendor

    def _detect_vendor_fallback(self):
        """Fallback vendor detection without gpu_utils"""
        try:
            result = subprocess.run(['nvidia-smi', '-L'], capture_output=True, text=True)
            if result.returncode == 0:
                return 'nvidia'
        except:
            pass
        try:
            result = subprocess.run(['rocm-smi', '-i'], capture_output=True, text=True)
            if result.returncode == 0:
                return 'amd'
        except:
            pass
        return 'unknown'

    def get_nvidia_smi_info(self):
        """Get basic GPU info from nvidia-smi"""
        try:
            # Get basic info
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=name,memory.total,power.limit,gpu_bus_id,vbios_version',
                 '--format=csv,noheader', '-i', str(self.gpu_id)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                parts = result.stdout.strip().split(', ')
                self.info['name'] = parts[0]
                self.info['memory'] = parts[1]
                self.info['power_limit'] = float(parts[2].replace(' W', ''))
                self.info['bus_id'] = parts[3].replace('0000:', '')
                self.info['vbios'] = parts[4]
        except Exception as e:
            print(f"Warning: Could not get nvidia-smi info: {e}")

    def get_rocm_smi_info(self):
        """Get basic GPU info from rocm-smi (AMD)"""
        try:
            # Get device info
            result = subprocess.run(
                ['rocm-smi', '-d', str(self.gpu_id), '-i'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                output = result.stdout

                # Parse card series/name
                card_match = re.search(r'Card series:\s*(.+)', output)
                if card_match:
                    self.info['name'] = card_match.group(1).strip()

                # Parse card model
                model_match = re.search(r'Card model:\s*(.+)', output)
                if model_match:
                    self.info['card_model'] = model_match.group(1).strip()

                # Parse card vendor
                vendor_match = re.search(r'Card vendor:\s*(.+)', output)
                if vendor_match:
                    self.info['card_vendor'] = vendor_match.group(1).strip()

                # Parse card SKU
                sku_match = re.search(r'Card SKU:\s*(.+)', output)
                if sku_match:
                    self.info['card_sku'] = sku_match.group(1).strip()

            # Get VRAM info
            result = subprocess.run(
                ['rocm-smi', '-d', str(self.gpu_id), '--showmeminfo', 'vram'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                total_match = re.search(r'Total Memory.*?:\s*(\d+)', result.stdout)
                if total_match:
                    total_bytes = int(total_match.group(1))
                    self.info['memory'] = f"{total_bytes // (1024*1024)} MiB"

            # Get power info
            result = subprocess.run(
                ['rocm-smi', '-d', str(self.gpu_id), '-P'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                max_power_match = re.search(r'Max.*?:\s*([\d.]+)', result.stdout)
                if max_power_match:
                    self.info['power_limit'] = float(max_power_match.group(1))

            # Get VBIOS info
            result = subprocess.run(
                ['rocm-smi', '-d', str(self.gpu_id), '-v'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                vbios_match = re.search(r'VBIOS version:\s*(.+)', result.stdout)
                if vbios_match:
                    self.info['vbios'] = vbios_match.group(1).strip()

            # Get bus ID
            result = subprocess.run(
                ['rocm-smi', '-d', str(self.gpu_id), '--showbus'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                bus_match = re.search(r'BDF:\s*(\S+)', result.stdout)
                if bus_match:
                    self.info['bus_id'] = bus_match.group(1).strip()

        except Exception as e:
            print(f"Warning: Could not get rocm-smi info: {e}")

    def get_pci_info(self):
        """Get detailed PCI subsystem information"""
        try:
            # Get PCI bus ID from nvidia-smi format to lspci format
            bus_id = self.info.get('bus_id', '01:00.0')

            # Get subsystem ID
            result = subprocess.run(
                ['lspci', '-vnn', '-s', bus_id],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                output = result.stdout

                # Extract vendor and device IDs
                vendor_match = re.search(r'\[([0-9a-fA-F]{4}):([0-9a-fA-F]{4})\]', output)
                if vendor_match:
                    self.info['vendor_id'] = vendor_match.group(1)
                    self.info['device_id'] = vendor_match.group(2)

                # Extract subsystem vendor and device IDs
                subsys_match = re.search(r'Subsystem:.*?\[([0-9a-fA-F]{4}):([0-9a-fA-F]{4})\]', output)
                if subsys_match:
                    self.info['subsystem_vendor_id'] = subsys_match.group(1)
                    self.info['subsystem_device_id'] = subsys_match.group(2)

                # Extract manufacturer name
                subsys_name_match = re.search(r'Subsystem: (.*?) \[', output)
                if subsys_name_match:
                    self.info['manufacturer'] = subsys_name_match.group(1).strip()

        except Exception as e:
            print(f"Warning: Could not get PCI info: {e}")

    def identify_model(self):
        """Identify specific GPU model from subsystem ID"""
        subsys_vendor = self.info.get('subsystem_vendor_id', '').upper()
        subsys_device = self.info.get('subsystem_device_id', '').upper()

        model_info = None

        # EVGA (3842)
        if subsys_vendor == '3842':
            model_info = EVGA_RTX_3090_MODELS.get(subsys_device)
            if model_info:
                self.info['manufacturer'] = 'EVGA'
                self.info['model_name'] = f"EVGA {model_info['name']}"
                self.info['model_tier'] = model_info['tier']
                self.info['rated_power'] = model_info['power']

        # ASUS (1043)
        elif subsys_vendor == '1043':
            model_info = ASUS_RTX_3090_MODELS.get(subsys_device)
            if model_info:
                self.info['manufacturer'] = 'ASUS'
                self.info['model_name'] = f"ASUS {model_info['name']}"
                self.info['model_tier'] = model_info['tier']
                self.info['rated_power'] = model_info['power']

        # Gigabyte (1458)
        elif subsys_vendor == '1458':
            model_info = GIGABYTE_RTX_3090_MODELS.get(subsys_device)
            if model_info:
                self.info['manufacturer'] = 'Gigabyte'
                self.info['model_name'] = f"Gigabyte {model_info['name']}"
                self.info['model_tier'] = model_info['tier']
                self.info['rated_power'] = model_info['power']

        # MSI (1462)
        elif subsys_vendor == '1462':
            model_info = MSI_RTX_3090_MODELS.get(subsys_device)
            if model_info:
                self.info['manufacturer'] = 'MSI'
                self.info['model_name'] = f"MSI {model_info['name']}"
                self.info['model_tier'] = model_info['tier']
                self.info['rated_power'] = model_info['power']

        # NVIDIA Reference (10de)
        elif subsys_vendor == '10DE':
            self.info['manufacturer'] = 'NVIDIA'
            self.info['model_name'] = f"NVIDIA {self.info.get('name', 'Unknown')} Founders Edition"
            self.info['model_tier'] = 'Reference'
            self.info['rated_power'] = 350

        if not model_info and subsys_vendor and subsys_device:
            self.info['model_name'] = f"Unknown variant (Subsystem: {subsys_vendor}:{subsys_device})"
            self.info['model_tier'] = 'Unknown'

    def identify_amd_model(self):
        """Identify specific AMD GPU model from subsystem ID"""
        subsys_vendor = self.info.get('subsystem_vendor_id', '').upper()
        subsys_device = self.info.get('subsystem_device_id', '').upper()
        device_id = self.info.get('device_id', '').upper()

        if HAS_GPU_UTILS:
            model_info = identify_amd_model(subsys_vendor, subsys_device, device_id)
            self.info.update(model_info)
        else:
            # Basic fallback for AMD
            if subsys_vendor == '1002':
                self.info['manufacturer'] = 'AMD'
                self.info['model_name'] = f"AMD {self.info.get('name', 'Unknown')} Reference"
                self.info['model_tier'] = 'Reference'
            elif subsys_vendor == '1DA2':
                self.info['manufacturer'] = 'Sapphire'
            elif subsys_vendor == '1682':
                self.info['manufacturer'] = 'XFX'
            elif subsys_vendor == '148C':
                self.info['manufacturer'] = 'PowerColor'
            elif subsys_vendor == '1043':
                self.info['manufacturer'] = 'ASUS'
            elif subsys_vendor == '1458':
                self.info['manufacturer'] = 'Gigabyte'
            elif subsys_vendor == '1462':
                self.info['manufacturer'] = 'MSI'
            else:
                self.info['manufacturer'] = 'Unknown'

            if 'model_name' not in self.info:
                self.info['model_name'] = f"Unknown AMD variant (Subsystem: {subsys_vendor}:{subsys_device})"
                self.info['model_tier'] = 'Unknown'

    def get_cuda_info(self):
        """Get CUDA capabilities (works for both NVIDIA CUDA and AMD ROCm via HIP)"""
        try:
            import torch
            if torch.cuda.is_available() and self.gpu_id < torch.cuda.device_count():
                props = torch.cuda.get_device_properties(self.gpu_id)
                self.info['cuda_name'] = props.name
                self.info['cuda_capability'] = f"{props.major}.{props.minor}"
                self.info['multiprocessors'] = props.multi_processor_count
                self.info['total_memory_gb'] = props.total_memory / 1024**3

                # Check if using ROCm/HIP
                if hasattr(torch.version, 'hip') and torch.version.hip is not None:
                    self.info['rocm_version'] = torch.version.hip
                    self.info['compute_api'] = 'ROCm/HIP'
                else:
                    self.info['cuda_version'] = torch.version.cuda
                    self.info['compute_api'] = 'CUDA'
        except:
            pass

    def get_rocm_info(self):
        """Get ROCm-specific capabilities for AMD GPUs"""
        try:
            import torch
            if torch.cuda.is_available() and self.gpu_id < torch.cuda.device_count():
                props = torch.cuda.get_device_properties(self.gpu_id)
                self.info['rocm_name'] = props.name
                self.info['gcn_arch'] = f"{props.major}.{props.minor}"
                self.info['compute_units'] = props.multi_processor_count
                self.info['total_memory_gb'] = props.total_memory / 1024**3

                if hasattr(torch.version, 'hip') and torch.version.hip is not None:
                    self.info['rocm_version'] = torch.version.hip
        except:
            pass

    def identify(self):
        """Run full identification"""
        print(f"Identifying GPU {self.gpu_id}...\n")

        vendor = self.vendor.value if HAS_GPU_UTILS else self.vendor

        if vendor == 'nvidia':
            self.get_nvidia_smi_info()
            self.get_pci_info()
            self.identify_model()
            self.get_cuda_info()
        elif vendor == 'amd':
            self.get_rocm_smi_info()
            self.get_pci_info()
            self.identify_amd_model()
            self.get_rocm_info()
        else:
            # Try both and see what works
            self.get_nvidia_smi_info()
            if not self.info.get('name'):
                self.get_rocm_smi_info()
            self.get_pci_info()
            if self.info.get('vendor_id', '').lower() == '10de':
                self.identify_model()
                self.get_cuda_info()
            elif self.info.get('vendor_id', '').lower() == '1002':
                self.identify_amd_model()
                self.get_rocm_info()

        return self.info

    def print_report(self):
        """Print detailed identification report"""
        print("=" * 80)
        print(f"GPU {self.gpu_id} IDENTIFICATION REPORT")
        print("=" * 80)
        print()

        # Basic Info
        print("BASIC INFORMATION:")
        print(f"  GPU Name:          {self.info.get('name', 'Unknown')}")
        print(f"  Manufacturer:      {self.info.get('manufacturer', 'Unknown')}")
        print(f"  Model:             {self.info.get('model_name', 'Unknown')}")
        print(f"  Model Tier:        {self.info.get('model_tier', 'Unknown')}")
        print()

        # Hardware Details
        print("HARDWARE DETAILS:")
        print(f"  Memory:            {self.info.get('memory', 'Unknown')}")
        print(f"  Power Limit:       {self.info.get('power_limit', 'Unknown')} W")
        if 'rated_power' in self.info:
            print(f"  Rated TDP:         {self.info.get('rated_power', 'Unknown')} W")
        print(f"  VBIOS Version:     {self.info.get('vbios', 'Unknown')}")
        print(f"  PCI Bus ID:        {self.info.get('bus_id', 'Unknown')}")
        print()

        # CUDA/ROCm Info
        vendor = self.info.get('vendor', 'unknown')
        if isinstance(vendor, str):
            vendor_str = vendor
        else:
            vendor_str = vendor.value if hasattr(vendor, 'value') else str(vendor)

        if vendor_str == 'amd' or 'rocm_version' in self.info or 'gcn_arch' in self.info:
            print("ROCm/HIP INFORMATION:")
            if 'gcn_arch' in self.info:
                print(f"  GCN Architecture:  {self.info.get('gcn_arch', 'Unknown')}")
            if 'compute_units' in self.info:
                print(f"  Compute Units:     {self.info.get('compute_units', 'Unknown')}")
            if 'total_memory_gb' in self.info:
                print(f"  Total Memory:      {self.info.get('total_memory_gb', 0):.2f} GB")
            if 'rocm_version' in self.info:
                print(f"  ROCm Version:      {self.info.get('rocm_version', 'Unknown')}")
            print()
        elif 'cuda_capability' in self.info:
            print("CUDA INFORMATION:")
            print(f"  CUDA Capability:   {self.info.get('cuda_capability', 'Unknown')}")
            print(f"  Multiprocessors:   {self.info.get('multiprocessors', 'Unknown')}")
            print(f"  Total Memory:      {self.info.get('total_memory_gb', 0):.2f} GB")
            if 'cuda_version' in self.info:
                print(f"  CUDA Version:      {self.info.get('cuda_version', 'Unknown')}")
            print()

        # PCI IDs
        print("PCI IDENTIFIERS:")
        print(f"  Vendor ID:         {self.info.get('vendor_id', 'Unknown')}")
        print(f"  Device ID:         {self.info.get('device_id', 'Unknown')}")
        print(f"  Subsystem Vendor:  {self.info.get('subsystem_vendor_id', 'Unknown')}")
        print(f"  Subsystem Device:  {self.info.get('subsystem_device_id', 'Unknown')}")
        print()

        # Model-Specific Info
        if self.info.get('model_tier'):
            print("MODEL CLASSIFICATION:")
            tier = self.info.get('model_tier')
            tier_desc = {
                'Base': 'Entry-level model with standard cooling',
                'Mid': 'Mid-tier model with enhanced cooling and mild overclock',
                'High': 'High-end model with premium cooling and factory overclock',
                'Flagship': 'Top-tier model with best cooling and highest factory overclock',
                'Extreme': 'Extreme enthusiast model with hybrid/water cooling',
                'Reference': 'NVIDIA reference design (Founders Edition)',
            }
            print(f"  Tier:              {tier}")
            print(f"  Description:       {tier_desc.get(tier, 'Unknown tier')}")
            print()

        print("=" * 80)

    def save_to_file(self, filename=None):
        """Save identification to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            gpu_name = self.info.get('model_name', 'Unknown').replace(' ', '_').replace('/', '-')
            filename = f"gpu_identification_GPU{self.gpu_id}_{timestamp}.json"

        self.info['identification_date'] = datetime.now().isoformat()

        with open(filename, 'w') as f:
            json.dump(self.info, f, indent=2)

        print(f"\nIdentification saved to: {filename}")
        return filename

def identify_all_gpus():
    """Identify all available GPUs"""
    # Detect vendor first
    if HAS_GPU_UTILS:
        vendor = detect_gpu_vendor()
        gpu_count = get_gpu_count(vendor)
        print(f"Detected GPU Vendor: {vendor.value.upper()}")
    else:
        vendor = None
        try:
            import torch
            gpu_count = torch.cuda.device_count()
        except:
            # Fallback to nvidia-smi
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=count', '--format=csv,noheader'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                gpu_count = int(result.stdout.strip())
            else:
                # Try rocm-smi
                result = subprocess.run(['rocm-smi', '-i'], capture_output=True, text=True)
                if result.returncode == 0:
                    gpu_count = len(re.findall(r'GPU\[(\d+)\]', result.stdout))
                    gpu_count = max(1, gpu_count)
                else:
                    gpu_count = 1

    print(f"Found {gpu_count} GPU(s)\n")

    identifiers = []
    for i in range(gpu_count):
        identifier = GPUIdentifier(i)
        identifier.identify()
        identifier.print_report()
        identifiers.append(identifier)

        if i < gpu_count - 1:
            print("\n")

    return identifiers

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='GPU Model Identification Tool - Identifies exact GPU model including manufacturer variant',
        epilog='Example: python identify_gpu.py --gpu 0 --save'
    )
    parser.add_argument('--gpu', type=int, help='GPU ID to identify (default: all GPUs)')
    parser.add_argument('--all', action='store_true', help='Identify all GPUs')
    parser.add_argument('--save', action='store_true', help='Save identification to JSON file')
    parser.add_argument('--json', action='store_true', help='Output as JSON only (no formatted report)')

    args = parser.parse_args()

    if args.all or args.gpu is None:
        # Identify all GPUs
        identifiers = identify_all_gpus()

        if args.save:
            for identifier in identifiers:
                identifier.save_to_file()
    else:
        # Identify specific GPU
        identifier = GPUIdentifier(args.gpu)
        identifier.identify()

        if args.json:
            print(json.dumps(identifier.info, indent=2))
        else:
            identifier.print_report()

            if args.save:
                identifier.save_to_file()

if __name__ == "__main__":
    main()
