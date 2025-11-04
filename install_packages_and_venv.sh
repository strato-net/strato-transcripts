#!/bin/bash
# ==============================================================================
# Python Environment Setup Script for RTX 5070 WhisperX Transcription
# ==============================================================================
#
# This script sets up the complete Python environment for WhisperX with RTX 5070.
# Run this AFTER installing NVIDIA drivers and rebooting.
#
# Usage:
#   ./install_packages_and_venv.sh
#
# After completion, manually configure HuggingFace token in setup_env.sh
#
# ==============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Python Environment Setup for RTX 5070${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Step 1: Verify NVIDIA driver
echo -e "${YELLOW}[1/10] Verifying NVIDIA driver installation...${NC}"
if ! command -v nvidia-smi &> /dev/null; then
    echo -e "${RED}ERROR: nvidia-smi not found. Please run install_nvidia_drivers.sh first.${NC}"
    exit 1
fi

if ! nvidia-smi &> /dev/null; then
    echo -e "${RED}ERROR: nvidia-smi failed. Driver may not be loaded correctly.${NC}"
    echo "Try rebooting or reinstalling the driver."
    exit 1
fi

echo -e "${GREEN}✓ NVIDIA driver verification:${NC}"
nvidia-smi --query-gpu=name,driver_version --format=csv,noheader
echo ""

# Step 2: Install system dependencies
echo -e "${YELLOW}[2/10] Installing system dependencies...${NC}"
sudo apt update
sudo apt install -y build-essential ffmpeg python3-dev python3-venv python3-pip git
echo -e "${GREEN}✓ System dependencies installed${NC}"
echo ""

# Step 3: Create Python virtual environment
echo -e "${YELLOW}[3/10] Creating Python virtual environment...${NC}"
if [ -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Warning: venv directory already exists. Removing...${NC}"
    rm -rf "$VENV_DIR"
fi
python3 -m venv "$VENV_DIR"
echo -e "${GREEN}✓ Virtual environment created at $VENV_DIR${NC}"
echo ""

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Step 4: Install PyTorch nightly
echo -e "${YELLOW}[4/10] Installing PyTorch nightly with CUDA 12.8...${NC}"
echo "This may take 2-5 minutes depending on internet speed..."
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
echo -e "${GREEN}✓ PyTorch nightly installed${NC}"
echo ""

# Step 5: Verify PyTorch installation
echo -e "${YELLOW}[5/10] Verifying PyTorch installation...${NC}"
python3 -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
if ! python3 -c "import torch; assert torch.cuda.is_available(), 'CUDA not available'" 2>/dev/null; then
    echo -e "${RED}ERROR: PyTorch cannot detect CUDA/GPU${NC}"
    exit 1
fi
echo -e "${GREEN}✓ PyTorch can use GPU${NC}"
echo ""

# Step 6: Install Python dependencies
echo -e "${YELLOW}[6/10] Installing Python dependencies from requirements-lock.txt...${NC}"
echo "This may take 5-10 minutes..."
if [ ! -f "$PROJECT_DIR/requirements-lock.txt" ]; then
    echo -e "${RED}ERROR: requirements-lock.txt not found in $PROJECT_DIR${NC}"
    exit 1
fi
pip install -r "$PROJECT_DIR/requirements-lock.txt"
echo -e "${GREEN}✓ Python dependencies installed${NC}"
echo ""

# Step 7: Apply WhisperX patches
echo -e "${YELLOW}[7/10] Applying WhisperX patches...${NC}"
WHISPERX_VADS="$VENV_DIR/lib/python3.12/site-packages/whisperx/vads/pyannote.py"
WHISPERX_ASR="$VENV_DIR/lib/python3.12/site-packages/whisperx/asr.py"

if [ ! -f "$WHISPERX_VADS" ]; then
    echo -e "${RED}ERROR: WhisperX vads/pyannote.py not found at $WHISPERX_VADS${NC}"
    exit 1
fi

if [ ! -f "$WHISPERX_ASR" ]; then
    echo -e "${RED}ERROR: WhisperX asr.py not found at $WHISPERX_ASR${NC}"
    exit 1
fi

# Apply patches
sed -i 's/use_auth_token/token/g' "$WHISPERX_VADS"
sed -i '412s/use_auth_token=None/token=None/' "$WHISPERX_ASR"

# Verify patches
VADS_COUNT=$(grep -c "use_auth_token" "$WHISPERX_VADS" || true)
if [ "$VADS_COUNT" -ne 0 ]; then
    echo -e "${RED}ERROR: Patch verification failed for vads/pyannote.py${NC}"
    exit 1
fi

echo -e "${GREEN}✓ WhisperX patches applied successfully${NC}"
echo ""

# Step 8: Configure LD_LIBRARY_PATH
echo -e "${YELLOW}[8/10] Configuring LD_LIBRARY_PATH...${NC}"
BASHRC="$HOME/.bashrc"
LD_PATH_LINE="export LD_LIBRARY_PATH=$PROJECT_DIR/venv/lib/python3.12/site-packages/nvidia/cudnn/lib:\$LD_LIBRARY_PATH"

if grep -q "nvidia/cudnn/lib" "$BASHRC" 2>/dev/null; then
    echo "LD_LIBRARY_PATH already configured in ~/.bashrc"
else
    echo "" >> "$BASHRC"
    echo "# Added by install_packages_and_venv.sh for PyTorch nightly cuDNN" >> "$BASHRC"
    echo "$LD_PATH_LINE" >> "$BASHRC"
    echo -e "${GREEN}✓ LD_LIBRARY_PATH added to ~/.bashrc${NC}"
fi

# Set for current session
export LD_LIBRARY_PATH="$VENV_DIR/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH"
echo -e "${GREEN}✓ LD_LIBRARY_PATH configured${NC}"
echo ""

# Step 9: Run verification tests
echo -e "${YELLOW}[9/10] Running verification tests...${NC}"

echo "Testing GPU..."
python3 -c "import torch; x = torch.randn(100,100, device='cuda'); print('✓ GPU test passed:', x.matmul(x).sum().item())"

echo "Testing cuDNN..."
python3 -c "import torch.backends.cudnn as cudnn; print('✓ cuDNN version:', cudnn.version()); print('✓ cuDNN enabled:', cudnn.is_available())"

echo "Testing WhisperX import..."
python3 -c "import whisperx; print('✓ WhisperX imported successfully')"

echo "Testing pyannote.audio import..."
python3 -c "from pyannote.audio import Pipeline; print('✓ pyannote.audio imported successfully')"

echo -e "${GREEN}✓ All verification tests passed${NC}"
echo ""

# Step 10: Setup environment file
echo -e "${YELLOW}[10/10] Checking setup_env.sh...${NC}"
if [ ! -f "$PROJECT_DIR/setup_env.sh" ]; then
    if [ -f "$PROJECT_DIR/setup_env.sh.example" ]; then
        cp "$PROJECT_DIR/setup_env.sh.example" "$PROJECT_DIR/setup_env.sh"
        echo -e "${GREEN}✓ Created setup_env.sh from example${NC}"
    else
        echo -e "${YELLOW}Warning: setup_env.sh.example not found${NC}"
    fi
else
    echo "setup_env.sh already exists"
fi
echo ""

# Final success message
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ Installation Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${YELLOW}MANUAL CONFIGURATION REQUIRED:${NC}"
echo ""
echo "1. Get a HuggingFace token:"
echo "   https://huggingface.co/settings/tokens"
echo ""
echo "2. Edit setup_env.sh and add your token:"
echo "   nano setup_env.sh"
echo ""
echo "3. Accept model agreements:"
echo "   - https://huggingface.co/pyannote/speaker-diarization-3.1"
echo "   - https://huggingface.co/pyannote/segmentation-3.0"
echo ""
echo -e "${GREEN}Ready to use!${NC}"
echo ""
echo "Usage:"
echo "  source setup_env.sh"
echo "  source venv/bin/activate"
echo "  python3 transcribe_with_diarization.py audio.mp3"
echo ""
echo "See SETUP_RTX_5070.md for complete documentation."
echo ""
