#!/usr/bin/env python3
"""
Batch GPU Testing Script
Runs benchmarks and stress tests on all available GPUs
"""
import torch
import subprocess
import argparse
import sys
from datetime import datetime

def get_available_gpus():
    """Get list of available GPU IDs"""
    if not torch.cuda.is_available():
        print("ERROR: No CUDA GPUs available")
        return []

    gpu_count = torch.cuda.device_count()
    gpus = []

    print(f"Found {gpu_count} GPU(s):\n")
    for i in range(gpu_count):
        props = torch.cuda.get_device_properties(i)
        print(f"GPU {i}: {props.name}")
        print(f"  Memory: {props.total_memory / 1024**3:.2f} GB")
        print(f"  CUDA Capability: {props.major}.{props.minor}")
        print()
        gpus.append({
            'id': i,
            'name': props.name,
            'memory': props.total_memory / 1024**3
        })

    return gpus

def run_benchmark(gpu_id, test_type='all'):
    """Run benchmark on specific GPU"""
    print(f"\n{'='*80}")
    print(f"Running benchmark on GPU {gpu_id}")
    print(f"{'='*80}\n")

    cmd = [
        sys.executable,
        'gpu_benchmarks/gpu_benchmark.py',
        '--gpu', str(gpu_id),
        '--test', test_type,
        '--save'
    ]

    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0

def run_stress_test(gpu_id, duration=60, test_type='all'):
    """Run stress test on specific GPU"""
    print(f"\n{'='*80}")
    print(f"Running stress test on GPU {gpu_id}")
    print(f"{'='*80}\n")

    cmd = [
        sys.executable,
        'gpu_benchmarks/gpu_stress_test.py',
        '--gpu', str(gpu_id),
        '--duration', str(duration),
        '--test', test_type,
        '--save'
    ]

    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0

def main():
    parser = argparse.ArgumentParser(description='Batch GPU Testing - Run tests on all GPUs')
    parser.add_argument('--gpus', type=str, help='Comma-separated list of GPU IDs (default: all)')
    parser.add_argument('--benchmark', action='store_true', help='Run benchmarks')
    parser.add_argument('--stress', action='store_true', help='Run stress tests')
    parser.add_argument('--duration', type=int, default=60, help='Stress test duration in seconds (default: 60)')
    parser.add_argument('--test-type', choices=['matmul', 'memory', 'compute', 'all'], default='all',
                        help='Test type for benchmarks (default: all)')
    parser.add_argument('--stress-type', choices=['compute', 'memory', 'all'], default='compute',
                        help='Stress test type (default: compute)')
    parser.add_argument('--compare', action='store_true', help='Generate comparison report after tests')

    args = parser.parse_args()

    # If neither specified, run both
    if not args.benchmark and not args.stress:
        args.benchmark = True
        args.stress = True

    print(f"{'#'*80}")
    print(f"Batch GPU Testing Suite")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*80}\n")

    # Get available GPUs
    all_gpus = get_available_gpus()
    if not all_gpus:
        return 1

    # Select GPUs to test
    if args.gpus:
        selected_ids = [int(x.strip()) for x in args.gpus.split(',')]
        selected_gpus = [gpu for gpu in all_gpus if gpu['id'] in selected_ids]
        if len(selected_gpus) != len(selected_ids):
            print("ERROR: Some specified GPU IDs not found")
            return 1
    else:
        selected_gpus = all_gpus

    print(f"Testing {len(selected_gpus)} GPU(s): {[gpu['id'] for gpu in selected_gpus]}\n")

    # Track results
    benchmark_results = {}
    stress_results = {}

    # Run benchmarks
    if args.benchmark:
        print(f"\n{'#'*80}")
        print(f"PHASE 1: BENCHMARKING")
        print(f"{'#'*80}\n")

        for gpu in selected_gpus:
            success = run_benchmark(gpu['id'], args.test_type)
            benchmark_results[gpu['id']] = success

            if not success:
                print(f"\n⚠️  WARNING: Benchmark failed for GPU {gpu['id']}")

    # Run stress tests
    if args.stress:
        print(f"\n{'#'*80}")
        print(f"PHASE 2: STRESS TESTING")
        print(f"{'#'*80}\n")

        for gpu in selected_gpus:
            success = run_stress_test(gpu['id'], args.duration, args.stress_type)
            stress_results[gpu['id']] = success

            if not success:
                print(f"\n⚠️  WARNING: Stress test failed for GPU {gpu['id']}")

            # Clear CUDA cache between tests
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

    # Summary
    print(f"\n{'#'*80}")
    print(f"BATCH TESTING SUMMARY")
    print(f"{'#'*80}\n")

    if benchmark_results:
        print("Benchmark Results:")
        for gpu_id, success in benchmark_results.items():
            status = "✓ PASSED" if success else "✗ FAILED"
            print(f"  GPU {gpu_id}: {status}")
        print()

    if stress_results:
        print("Stress Test Results:")
        for gpu_id, success in stress_results.items():
            status = "✓ PASSED" if success else "✗ FAILED"
            print(f"  GPU {gpu_id}: {status}")
        print()

    # Generate comparison report
    if args.compare:
        print(f"\n{'#'*80}")
        print(f"GENERATING COMPARISON REPORT")
        print(f"{'#'*80}\n")

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"comparison_report_{timestamp}.txt"

        cmd = [
            sys.executable,
            'gpu_benchmarks/compare_results.py',
            '--output', output_file
        ]

        subprocess.run(cmd)

    print(f"\n{'#'*80}")
    print(f"Batch testing completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*80}\n")

    # Return success if all tests passed
    all_passed = all(benchmark_results.values()) and all(stress_results.values())
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
