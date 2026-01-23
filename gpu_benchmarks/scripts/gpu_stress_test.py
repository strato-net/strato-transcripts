#!/usr/bin/env python3
"""
GPU Stress Test and Stability Testing
Performs intensive compute operations to test GPU stability
Supports both NVIDIA (CUDA) and AMD (ROCm) GPUs
"""
import torch
import time
import argparse
from datetime import datetime, timedelta

# Import unified GPU utilities
try:
    from gpu_utils import GPUVendor, detect_gpu_vendor, get_gpu_temperature
    HAS_GPU_UTILS = True
except ImportError:
    HAS_GPU_UTILS = False

def get_compute_backend():
    """Determine if using CUDA or ROCm"""
    if hasattr(torch.version, 'hip') and torch.version.hip is not None:
        return 'rocm', torch.version.hip
    elif torch.version.cuda is not None:
        return 'cuda', torch.version.cuda
    else:
        return 'unknown', 'unknown'

def get_temperature_safe(gpu_id=0):
    """Get GPU temperature with fallback"""
    if HAS_GPU_UTILS:
        temp = get_gpu_temperature(gpu_id)
        if temp is not None:
            return temp

    # Fallback to PyTorch method (NVIDIA only)
    try:
        return torch.cuda.temperature(gpu_id)
    except:
        return None

class GPUStressTest:
    def __init__(self, gpu_id=0):
        self.device = torch.device(f'cuda:{gpu_id}')
        self.gpu_id = gpu_id
        torch.cuda.set_device(self.device)

        # Detect compute backend (CUDA or ROCm)
        self.backend, self.backend_version = get_compute_backend()

        # Detect vendor
        if HAS_GPU_UTILS:
            self.vendor = detect_gpu_vendor()
        else:
            self.vendor = 'nvidia' if self.backend == 'cuda' else 'amd'

        # Get GPU properties
        props = torch.cuda.get_device_properties(self.device)
        self.gpu_name = props.name
        self.total_memory = props.total_memory / 1024**3  # GB
        self.gpu_props = {
            'id': gpu_id,
            'name': props.name,
            'total_memory_gb': self.total_memory,
            'multiprocessor_count': props.multi_processor_count,
        }

        # Add vendor-specific naming
        if self.backend == 'rocm':
            self.gpu_props['gcn_arch'] = f"{props.major}.{props.minor}"
        else:
            self.gpu_props['cuda_capability'] = f"{props.major}.{props.minor}"

        vendor_str = self.vendor.value.upper() if hasattr(self.vendor, 'value') else str(self.vendor).upper()
        print(f"GPU {gpu_id}: {self.gpu_name}")
        print(f"Vendor: {vendor_str} ({self.backend.upper()})")
        print(f"Total Memory: {self.total_memory:.2f} GB")

    def matrix_multiply_stress(self, size=8192, duration=60, memory_fraction=0.8):
        """
        Stress test using large matrix multiplications

        Args:
            size: Matrix dimension
            duration: Test duration in seconds
            memory_fraction: Fraction of GPU memory to use
        """
        print(f"\n{'='*80}")
        print(f"Matrix Multiplication Stress Test")
        print(f"Matrix size: {size}x{size}")
        print(f"Duration: {duration}s")
        print(f"{'='*80}\n")

        # Calculate matrix size to use target memory fraction
        element_size = 4  # float32
        max_elements = int((self.total_memory * memory_fraction * 1024**3) / element_size / 3)  # 3 matrices
        actual_size = int(max_elements ** 0.5)

        if actual_size < size:
            size = actual_size
            print(f"Adjusted matrix size to {size}x{size} to fit in {memory_fraction*100}% of GPU memory")

        # Create test matrices
        print("Allocating matrices...")
        A = torch.randn(size, size, device=self.device, dtype=torch.float32)
        B = torch.randn(size, size, device=self.device, dtype=torch.float32)

        start_time = time.time()
        end_time = start_time + duration
        iterations = 0
        errors = 0

        print(f"Starting stress test at {datetime.now().strftime('%H:%M:%S')}")
        print("Press Ctrl+C to stop early\n")

        try:
            while time.time() < end_time:
                try:
                    # Perform intensive matrix multiplication
                    C = torch.matmul(A, B)

                    # Verify computation (basic sanity check)
                    if torch.isnan(C).any() or torch.isinf(C).any():
                        errors += 1
                        print(f"ERROR: NaN or Inf detected at iteration {iterations}")

                    iterations += 1

                    # Progress update every 10 iterations
                    if iterations % 10 == 0:
                        elapsed = time.time() - start_time
                        remaining = duration - elapsed
                        temp = get_temperature_safe(self.gpu_id)
                        mem_used = torch.cuda.memory_allocated(self.device) / 1024**3
                        temp_str = f"{temp}°C" if temp is not None else "N/A"
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                              f"Iteration: {iterations} | "
                              f"Time remaining: {remaining:.1f}s | "
                              f"Temp: {temp_str} | "
                              f"Memory: {mem_used:.2f}GB")

                    del C
                    torch.cuda.synchronize()

                except RuntimeError as e:
                    errors += 1
                    print(f"ERROR at iteration {iterations}: {e}")
                    break

        except KeyboardInterrupt:
            print("\n\nTest interrupted by user")

        # Cleanup
        del A, B
        torch.cuda.empty_cache()

        # Results
        total_time = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"Stress Test Results")
        print(f"{'='*80}")
        print(f"Duration: {total_time:.2f}s")
        print(f"Iterations completed: {iterations}")
        print(f"Average iteration time: {total_time/iterations:.3f}s" if iterations > 0 else "N/A")
        print(f"Errors encountered: {errors}")
        print(f"Status: {'PASSED' if errors == 0 else 'FAILED'}")
        print(f"{'='*80}\n")

        return errors == 0

    def memory_stress_test(self, duration=60):
        """Test GPU memory allocation and deallocation"""
        print(f"\n{'='*80}")
        print(f"Memory Stress Test")
        print(f"Duration: {duration}s")
        print(f"{'='*80}\n")

        start_time = time.time()
        end_time = start_time + duration
        iterations = 0
        errors = 0

        try:
            while time.time() < end_time:
                try:
                    # Allocate large chunk of memory
                    chunk_size = int(self.total_memory * 0.7 * 1024**3 / 4)  # 70% of GPU memory
                    tensor = torch.randn(chunk_size, device=self.device, dtype=torch.float32)

                    # Perform operations
                    result = tensor * 2.0 + 1.0

                    # Verify
                    if torch.isnan(result).any():
                        errors += 1
                        print(f"ERROR: NaN detected at iteration {iterations}")

                    iterations += 1

                    if iterations % 10 == 0:
                        elapsed = time.time() - start_time
                        remaining = duration - elapsed
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                              f"Iteration: {iterations} | "
                              f"Time remaining: {remaining:.1f}s")

                    # Cleanup
                    del tensor, result
                    torch.cuda.empty_cache()

                except RuntimeError as e:
                    errors += 1
                    print(f"ERROR at iteration {iterations}: {e}")
                    break

        except KeyboardInterrupt:
            print("\n\nTest interrupted by user")

        total_time = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"Memory Test Results")
        print(f"{'='*80}")
        print(f"Duration: {total_time:.2f}s")
        print(f"Iterations completed: {iterations}")
        print(f"Errors encountered: {errors}")
        print(f"Status: {'PASSED' if errors == 0 else 'FAILED'}")
        print(f"{'='*80}\n")

        return errors == 0

def main():
    import json

    parser = argparse.ArgumentParser(description='GPU Stress Testing Tool')
    parser.add_argument('--gpu', type=int, default=0, help='GPU ID to test (default: 0)')
    parser.add_argument('--duration', type=int, default=60, help='Test duration in seconds (default: 60)')
    parser.add_argument('--matrix-size', type=int, default=8192, help='Matrix size for compute test (default: 8192)')
    parser.add_argument('--test', choices=['compute', 'memory', 'all'], default='all', help='Test type (default: all)')
    parser.add_argument('--save', action='store_true', help='Save results to JSON file')

    args = parser.parse_args()

    timestamp = datetime.now()

    print(f"\n{'#'*80}")
    print(f"GPU Stress Test Suite")
    print(f"Started at: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*80}\n")

    tester = GPUStressTest(gpu_id=args.gpu)

    results = {}

    if args.test in ['compute', 'all']:
        results['compute'] = tester.matrix_multiply_stress(
            size=args.matrix_size,
            duration=args.duration
        )

    if args.test in ['memory', 'all']:
        results['memory'] = tester.memory_stress_test(duration=args.duration)

    # Final summary
    print(f"\n{'#'*80}")
    print(f"Final Summary")
    print(f"{'#'*80}")
    for test_name, passed in results.items():
        status = "PASSED ✓" if passed else "FAILED ✗"
        print(f"{test_name.capitalize()} Test: {status}")
    print(f"{'#'*80}\n")

    overall_pass = all(results.values())

    # Save results if requested
    if args.save:
        # Build test metadata with correct backend info
        test_metadata = {
            'timestamp': timestamp.isoformat(),
            'date': timestamp.strftime('%Y-%m-%d'),
            'time': timestamp.strftime('%H:%M:%S'),
            'duration': args.duration,
            'matrix_size': args.matrix_size,
            'test_type': args.test,
            'pytorch_version': torch.__version__,
            'compute_backend': tester.backend,
        }

        # Add backend-specific version
        if tester.backend == 'rocm':
            test_metadata['rocm_version'] = tester.backend_version
        else:
            test_metadata['cuda_version'] = tester.backend_version

        test_results = {
            'gpu_info': tester.gpu_props,
            'test_metadata': test_metadata,
            'test_results': results,
            'overall_status': 'PASSED' if overall_pass else 'FAILED'
        }

        gpu_name_safe = tester.gpu_name.replace(' ', '_').replace('/', '-')
        filename = f"stress_test_GPU{tester.gpu_id}_{gpu_name_safe}_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(test_results, f, indent=2)
        print(f"Results saved to: {filename}\n")

    return 0 if overall_pass else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
