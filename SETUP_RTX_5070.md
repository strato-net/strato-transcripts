# RTX 5070 Setup Guide for WhisperX Transcription

**Automated setup for Ubuntu 24.04 LTS with NVIDIA RTX 5070 (Blackwell architecture)**

---

## Setup Instructions

### Step 1: Install NVIDIA Drivers
```bash
sudo ./install_nvidia_drivers.sh
sudo reboot
```

**What it does:**
- Updates system packages
- Installs NVIDIA driver 565+ (required for RTX 5070)
- Verifies installation

### Step 2: Setup Python Environment (after reboot)
```bash
./install_packages_and_venv.sh
```

**What it does:**
- Installs system dependencies (build-essential, ffmpeg, python3-dev, git)
- Creates Python virtual environment
- Installs PyTorch nightly with CUDA 12.8
- Installs all Python dependencies from requirements-lock.txt
- Applies WhisperX patches automatically
- Configures LD_LIBRARY_PATH in ~/.bashrc
- Runs verification tests

### Step 3: Configure HuggingFace Token
```bash
nano setup_env.sh
```

Add your HF_TOKEN from https://huggingface.co/settings/tokens

Accept model agreements:
- https://huggingface.co/pyannote/speaker-diarization-3.1
- https://huggingface.co/pyannote/segmentation-3.0

**Setup complete!**

---

## Hardware Requirements

- **GPU:** NVIDIA GeForce RTX 5070 (Blackwell architecture, sm_120)
- **RAM:** 16GB minimum, 32GB recommended
- **Storage:** 50GB free space for models and processing
- **CPU:** Modern multi-core processor (8+ cores recommended)

---

## System Requirements

- **OS:** Ubuntu 24.04 LTS (fresh install)
- **Kernel:** Linux 6.8+
- **Python:** 3.12 (comes with Ubuntu 24.04)

---

## Running Transcription

```bash
# Load environment
source setup_env.sh
source venv/bin/activate

# Run transcription
python3 transcribe_with_diarization.py path/to/audio.mp3
```

**Output:** `path/to/audio_transcript_with_speakers.txt`

---

## Performance Benchmarks

**Hardware:** NVIDIA GeForce RTX 5070 (12GB VRAM, Blackwell/sm_120)

**79-minute audio:**
- Transcription: 98.7 seconds (~48x realtime)
- Diarization: 208.6 seconds
- Total: 314.7 seconds (5.2 minutes, ~15x realtime)

**58-minute audio:**
- Transcription: 65 seconds (~53x realtime)

**GPU Performance:**
- Utilization: 90-95%
- VRAM usage: 8-10GB peak
- ~95-150x faster than manual transcription

---

## Technical Details

### Why PyTorch Nightly?

RTX 5070 uses Blackwell architecture (sm_120) released in 2025. Only PyTorch nightly builds have sm_120 support.

### Why LD_LIBRARY_PATH?

PyTorch nightly bundles cuDNN but doesn't configure library paths. This is a nightly packaging issue that will be fixed in PyTorch 2.10+ stable (Q1 2026).

### Requirements Files

- **requirements.txt** - 6 direct dependencies, flexible versions
- **requirements-lock.txt** - 155+ packages with exact versions

Generate lock file: `pip freeze > requirements-lock.txt`

---

## Troubleshooting

### nvidia-smi doesn't work
```bash
sudo ubuntu-drivers install --reinstall
sudo reboot
```

### PyTorch can't find GPU
```bash
pip uninstall torch torchvision torchaudio -y
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
```

### "Unable to load libcudnn_cnn.so.9"
```bash
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH
```

### WhisperX API errors
The `install_packages_and_venv.sh` script should have applied patches automatically. If not:
```bash
sed -i 's/use_auth_token/token/g' venv/lib/python3.12/site-packages/whisperx/vads/pyannote.py
sed -i '412s/use_auth_token=None/token=None/' venv/lib/python3.12/site-packages/whisperx/asr.py
```

### Out of memory
Close other GPU applications or edit transcribe_with_diarization.py to use smaller model:
```python
model = whisperx.load_model("medium", device, compute_type="float16")
```

---

## Version Compatibility

| Component | Version | Why |
|-----------|---------|-----|
| NVIDIA Driver | 565+ | RTX 50-series support |
| CUDA (bundled) | 12.8 | sm_120 compute capability |
| PyTorch | 2.10.0.dev nightly | sm_120 support |
| pyannote.audio | 4.0.1+ | PyTorch 2.10+ compatibility |
| NumPy | 2.0+ | pyannote.audio requirement |

---

**Status:** ✅ Fully working, production-ready

**Last Updated:** November 4, 2025

**Support:**
- Check troubleshooting above
- Review README.md
- Open an issue on the repository
