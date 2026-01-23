#!/bin/bash
# GPU Benchmarking Suite - Interactive Menu

# Activate virtual environment
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BENCHMARK_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_DIR="$(dirname "$BENCHMARK_DIR")"

if [ -f "$PROJECT_DIR/venv/bin/activate" ]; then
    source "$PROJECT_DIR/venv/bin/activate"
else
    echo "Error: Virtual environment not found at $PROJECT_DIR/venv"
    exit 1
fi

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

show_menu() {
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}         GPU Benchmarking & Stability Testing${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${GREEN}Monitoring Tools:${NC}"
    echo "  1) GPU Monitor (real-time dashboard)"
    echo "  2) Quick GPU Status (gpustat)"
    echo "  3) NVIDIA SMI"
    echo ""
    echo -e "${GREEN}Single GPU Benchmarking:${NC}"
    echo "  4) Full Performance Benchmark (saves results)"
    echo "  5) Quick Performance Benchmark"
    echo "  6) Matrix Multiplication Benchmark Only"
    echo "  7) Memory Bandwidth Benchmark Only"
    echo ""
    echo -e "${GREEN}Single GPU Stress Testing:${NC}"
    echo "  8) Full Stability Test (60 seconds)"
    echo "  9) Extended Stability Test (10 minutes)"
    echo " 10) Long Stability Test (1 hour)"
    echo " 11) Compute Stress Test Only"
    echo ""
    echo -e "${GREEN}Multi-GPU Testing:${NC}"
    echo " 20) List All Available GPUs"
    echo " 21) Test All GPUs (Benchmark + Stress)"
    echo " 22) Benchmark All GPUs"
    echo " 23) Stress Test All GPUs"
    echo " 24) Compare Results from Multiple GPUs"
    echo ""
    echo " 0) Exit"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

run_command() {
    echo -e "\n${YELLOW}Running: $1${NC}\n"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    eval "$1"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Main loop
while true; do
    clear
    show_menu
    read -p "Select option: " choice

    case $choice in
        1)
            run_command "python $SCRIPT_DIR/gpu_monitor.py"
            ;;
        2)
            run_command "gpustat"
            read -p "Press Enter to continue..."
            ;;
        3)
            run_command "nvidia-smi"
            read -p "Press Enter to continue..."
            ;;
        4)
            run_command "python $SCRIPT_DIR/gpu_benchmark.py --save"
            read -p "Press Enter to continue..."
            ;;
        5)
            run_command "python $SCRIPT_DIR/gpu_benchmark.py"
            read -p "Press Enter to continue..."
            ;;
        6)
            run_command "python $SCRIPT_DIR/gpu_benchmark.py --test matmul"
            read -p "Press Enter to continue..."
            ;;
        7)
            run_command "python $SCRIPT_DIR/gpu_benchmark.py --test memory"
            read -p "Press Enter to continue..."
            ;;
        8)
            run_command "python $SCRIPT_DIR/gpu_stress_test.py --duration 60"
            read -p "Press Enter to continue..."
            ;;
        9)
            run_command "python $SCRIPT_DIR/gpu_stress_test.py --duration 600"
            read -p "Press Enter to continue..."
            ;;
        10)
            run_command "python $SCRIPT_DIR/gpu_stress_test.py --duration 3600"
            read -p "Press Enter to continue..."
            ;;
        11)
            run_command "python $SCRIPT_DIR/gpu_stress_test.py --test compute --duration 300 --save"
            read -p "Press Enter to continue..."
            ;;
        20)
            run_command "python $SCRIPT_DIR/test_all_gpus.py --help && echo '' && python -c 'import torch; print(f\"Available GPUs: {torch.cuda.device_count()}\"); [print(f\"  GPU {i}: {torch.cuda.get_device_properties(i).name}\") for i in range(torch.cuda.device_count())]'"
            read -p "Press Enter to continue..."
            ;;
        21)
            echo -e "\n${YELLOW}This will run full benchmarks and stress tests on ALL GPUs${NC}"
            read -p "Enter stress test duration in seconds (default: 60): " duration
            duration=${duration:-60}
            run_command "python $SCRIPT_DIR/test_all_gpus.py --benchmark --stress --duration $duration --compare"
            read -p "Press Enter to continue..."
            ;;
        22)
            run_command "python $SCRIPT_DIR/test_all_gpus.py --benchmark --compare"
            read -p "Press Enter to continue..."
            ;;
        23)
            echo -e "\n${YELLOW}This will run stress tests on ALL GPUs${NC}"
            read -p "Enter stress test duration in seconds (default: 60): " duration
            duration=${duration:-60}
            run_command "python $SCRIPT_DIR/test_all_gpus.py --stress --duration $duration --compare"
            read -p "Press Enter to continue..."
            ;;
        24)
            run_command "python $SCRIPT_DIR/compare_results.py"
            read -p "Press Enter to continue..."
            ;;
        0)
            echo -e "\n${GREEN}Goodbye!${NC}\n"
            exit 0
            ;;
        *)
            echo -e "\n${RED}Invalid option. Press Enter to try again...${NC}"
            read
            ;;
    esac
done
