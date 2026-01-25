#!/usr/bin/env python3
"""
Multi-GPU Benchmark Results Comparison Tool
Compares performance across multiple GPU benchmark results
"""
import json
import glob
import argparse
from datetime import datetime
from pathlib import Path

class ResultsComparator:
    def __init__(self):
        self.benchmark_results = []
        self.stress_results = []

    def load_benchmark_results(self, pattern="benchmark_GPU*.json"):
        """Load all benchmark result files matching pattern"""
        files = sorted(glob.glob(pattern))
        for file in files:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    data['_filename'] = file
                    self.benchmark_results.append(data)
            except Exception as e:
                print(f"Warning: Could not load {file}: {e}")

        print(f"Loaded {len(self.benchmark_results)} benchmark result files")
        return len(self.benchmark_results)

    def load_stress_results(self, pattern="stress_test_GPU*.json"):
        """Load all stress test result files matching pattern"""
        files = sorted(glob.glob(pattern))
        for file in files:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    data['_filename'] = file
                    self.stress_results.append(data)
            except Exception as e:
                print(f"Warning: Could not load {file}: {e}")

        print(f"Loaded {len(self.stress_results)} stress test result files")
        return len(self.stress_results)

    def compare_benchmarks(self):
        """Generate comparison report for benchmark results"""
        if not self.benchmark_results:
            print("No benchmark results to compare")
            return

        print(f"\n{'='*100}")
        print("BENCHMARK RESULTS COMPARISON")
        print(f"{'='*100}\n")

        # Extract GPU info
        gpus = []
        for result in self.benchmark_results:
            gpu_info = result.get('gpu_info', {})
            test_meta = result.get('test_metadata', {})
            gpus.append({
                'id': gpu_info.get('id', 'N/A'),
                'name': gpu_info.get('name', 'Unknown'),
                'memory': gpu_info.get('total_memory_gb', 'N/A'),
                'cuda_cap': gpu_info.get('cuda_capability', 'N/A'),
                'date': test_meta.get('date', 'N/A'),
                'time': test_meta.get('time', 'N/A'),
                'results': result.get('benchmark_results', {}),
                'filename': result.get('_filename', 'N/A')
            })

        # Print GPU Summary
        print("GPU SUMMARY:")
        print(f"{'ID':<5} {'GPU Name':<35} {'Memory':<10} {'CUDA':<8} {'Test Date':<12} {'Test Time':<10}")
        print("-" * 100)
        for gpu in gpus:
            print(f"{gpu['id']:<5} {gpu['name']:<35} {gpu['memory']:<10.2f} GB {gpu['cuda_cap']:<8} {gpu['date']:<12} {gpu['time']:<10}")

        # Compare Matrix Multiplication Performance
        print(f"\n{'='*100}")
        print("MATRIX MULTIPLICATION PERFORMANCE (GFLOPS)")
        print(f"{'='*100}")

        matrix_sizes = [1024, 2048, 4096, 8192]
        print(f"\n{'Size':<12}", end="")
        for gpu in gpus:
            print(f"GPU{gpu['id']} ({gpu['name'][:20]}...)"[:25].ljust(25), end="")
        print()
        print("-" * 100)

        for size in matrix_sizes:
            print(f"{size}x{size:<7}", end="")
            for gpu in gpus:
                matmul_results = gpu['results'].get('matmul', [])
                gflops = 'N/A'
                for res in matmul_results:
                    if res.get('size') == size:
                        gflops = f"{res.get('gflops', 0):.1f}"
                        break
                print(f"{gflops:<25}", end="")
            print()

        # Find best performer for each size
        print(f"\nBest Performer by Matrix Size:")
        for size in matrix_sizes:
            best_gpu = None
            best_gflops = 0
            for gpu in gpus:
                matmul_results = gpu['results'].get('matmul', [])
                for res in matmul_results:
                    if res.get('size') == size:
                        gflops = res.get('gflops', 0)
                        if gflops > best_gflops:
                            best_gflops = gflops
                            best_gpu = gpu
                        break
            if best_gpu:
                print(f"  {size}x{size}: GPU{best_gpu['id']} ({best_gpu['name']}) - {best_gflops:.1f} GFLOPS")

        # Compare Memory Bandwidth
        print(f"\n{'='*100}")
        print("MEMORY BANDWIDTH (GB/s) - Host to Device")
        print(f"{'='*100}")

        transfer_sizes = [1, 10, 100, 1000]
        print(f"\n{'Size (MB)':<12}", end="")
        for gpu in gpus:
            print(f"GPU{gpu['id']} ({gpu['name'][:20]}...)"[:25].ljust(25), end="")
        print()
        print("-" * 100)

        for size in transfer_sizes:
            print(f"{size:<12}", end="")
            for gpu in gpus:
                bw_results = gpu['results'].get('memory_bandwidth', [])
                bandwidth = 'N/A'
                for res in bw_results:
                    if res.get('size_mb') == size:
                        bandwidth = f"{res.get('h2d_bandwidth_gbps', 0):.2f}"
                        break
                print(f"{bandwidth:<25}", end="")
            print()

        # Compare Compute Throughput
        print(f"\n{'='*100}")
        print("COMPUTE THROUGHPUT (GOPS)")
        print(f"{'='*100}")

        operations = ['Addition', 'Multiplication', 'Division', 'Sqrt', 'Exp', 'Sin']
        print(f"\n{'Operation':<15}", end="")
        for gpu in gpus:
            print(f"GPU{gpu['id']} ({gpu['name'][:20]}...)"[:25].ljust(25), end="")
        print()
        print("-" * 100)

        for op in operations:
            print(f"{op:<15}", end="")
            for gpu in gpus:
                compute_results = gpu['results'].get('compute_throughput', {})
                throughput = compute_results.get(op, {}).get('throughput_gops', 'N/A')
                if throughput != 'N/A':
                    throughput = f"{throughput:.2f}"
                print(f"{throughput:<25}", end="")
            print()

        # Overall Performance Ranking
        print(f"\n{'='*100}")
        print("OVERALL PERFORMANCE RANKING (Based on 8192x8192 MatMul)")
        print(f"{'='*100}\n")

        ranked_gpus = []
        for gpu in gpus:
            matmul_results = gpu['results'].get('matmul', [])
            for res in matmul_results:
                if res.get('size') == 8192:
                    ranked_gpus.append({
                        'gpu': gpu,
                        'gflops': res.get('gflops', 0)
                    })
                    break

        ranked_gpus.sort(key=lambda x: x['gflops'], reverse=True)

        for i, item in enumerate(ranked_gpus, 1):
            gpu = item['gpu']
            gflops = item['gflops']
            print(f"{i}. GPU{gpu['id']}: {gpu['name']}")
            print(f"   Performance: {gflops:.1f} GFLOPS")
            print(f"   Memory: {gpu['memory']:.2f} GB | CUDA: {gpu['cuda_cap']}")
            print()

    def compare_stress_tests(self):
        """Generate comparison report for stress test results"""
        if not self.stress_results:
            print("No stress test results to compare")
            return

        print(f"\n{'='*100}")
        print("STRESS TEST RESULTS COMPARISON")
        print(f"{'='*100}\n")

        # Extract GPU info and results
        gpus = []
        for result in self.stress_results:
            gpu_info = result.get('gpu_info', {})
            test_meta = result.get('test_metadata', {})
            test_res = result.get('test_results', {})
            gpus.append({
                'id': gpu_info.get('id', 'N/A'),
                'name': gpu_info.get('name', 'Unknown'),
                'memory': gpu_info.get('total_memory_gb', 'N/A'),
                'date': test_meta.get('date', 'N/A'),
                'time': test_meta.get('time', 'N/A'),
                'duration': test_meta.get('duration', 'N/A'),
                'compute_passed': test_res.get('compute', False),
                'memory_passed': test_res.get('memory', False),
                'overall_status': result.get('overall_status', 'UNKNOWN'),
                'filename': result.get('_filename', 'N/A')
            })

        # Print GPU Summary
        print("STRESS TEST SUMMARY:")
        print(f"{'ID':<5} {'GPU Name':<35} {'Duration':<10} {'Compute':<10} {'Memory':<10} {'Overall':<10}")
        print("-" * 100)
        for gpu in gpus:
            compute_status = "✓ PASS" if gpu['compute_passed'] else "✗ FAIL"
            memory_status = "✓ PASS" if gpu['memory_passed'] else "✗ FAIL"
            overall = "✓ PASS" if gpu['overall_status'] == 'PASSED' else "✗ FAIL"
            print(f"{gpu['id']:<5} {gpu['name']:<35} {gpu['duration']:<10}s {compute_status:<10} {memory_status:<10} {overall:<10}")

        # Summary statistics
        total_gpus = len(gpus)
        passed_gpus = sum(1 for gpu in gpus if gpu['overall_status'] == 'PASSED')
        failed_gpus = total_gpus - passed_gpus

        print(f"\n{'='*100}")
        print("STABILITY SUMMARY:")
        print(f"{'='*100}")
        print(f"Total GPUs Tested: {total_gpus}")
        print(f"Passed: {passed_gpus} ({passed_gpus/total_gpus*100:.1f}%)")
        print(f"Failed: {failed_gpus} ({failed_gpus/total_gpus*100:.1f}%)")

        if failed_gpus > 0:
            print(f"\n⚠️  WARNING: {failed_gpus} GPU(s) failed stability testing!")
            print("Review individual test results for details.")

    def generate_full_report(self, output_file=None):
        """Generate complete comparison report"""
        report = []

        # Redirect print to capture output
        import sys
        from io import StringIO

        old_stdout = sys.stdout
        sys.stdout = captured = StringIO()

        self.compare_benchmarks()
        self.compare_stress_tests()

        sys.stdout = old_stdout
        report_text = captured.getvalue()

        print(report_text)

        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)
            print(f"\n\nFull report saved to: {output_file}")

        return report_text

def main():
    parser = argparse.ArgumentParser(description='Compare GPU benchmark and stress test results')
    parser.add_argument('--benchmark-pattern', default='benchmark_GPU*.json',
                        help='Pattern for benchmark result files (default: benchmark_GPU*.json)')
    parser.add_argument('--stress-pattern', default='stress_test_GPU*.json',
                        help='Pattern for stress test result files (default: stress_test_GPU*.json)')
    parser.add_argument('--output', '-o', help='Save comparison report to file')
    parser.add_argument('--benchmark-only', action='store_true', help='Compare only benchmark results')
    parser.add_argument('--stress-only', action='store_true', help='Compare only stress test results')

    args = parser.parse_args()

    comparator = ResultsComparator()

    # Load results
    if not args.stress_only:
        comparator.load_benchmark_results(args.benchmark_pattern)

    if not args.stress_only:
        comparator.load_stress_results(args.stress_pattern)

    # Generate comparisons
    if args.output:
        comparator.generate_full_report(args.output)
    else:
        if not args.stress_only:
            comparator.compare_benchmarks()
        if not args.benchmark_only:
            comparator.compare_stress_tests()

if __name__ == "__main__":
    main()
