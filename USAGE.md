# WhisperX Transcription Usage Guide

## Quick Start

### 1. Set up the environment (one-time setup)

```bash
# Copy the example and add your Hugging Face token
cp setup_env.sh.example setup_env.sh
# Edit setup_env.sh and replace 'your_huggingface_token_here' with your actual token

# Or if setup_env.sh already exists with your token, just source it
source setup_env.sh

# Activate the virtual environment
source venv/bin/activate
```

### 2. Run transcription with speaker diarization

```bash
# Run the pipeline
python3 diarize_and_combine.py \
    source/videos/raw-audio/institutions_want_tokens_how_is_ethereum_keeping_up.mp3 \
    existing_transcript.txt

# Output will be saved as:
# source/videos/raw-audio/institutions_want_tokens_how_is_ethereum_keeping_up_transcript_with_speakers.txt
```

### 3. Alternative: Using environment variable directly

```bash
# Set the token directly (not recommended for permanent use)
export HF_TOKEN="your_token_here"

# Or add to your ~/.bashrc or ~/.zshrc for permanent setup:
echo 'export HF_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc

# Then run the script
source venv/bin/activate
python3 diarize_and_combine.py audio.mp3 transcript.txt
```

## Environment Requirements

- Python 3.8+
- CUDA-capable GPU (highly recommended)
- Hugging Face account with accepted model agreements

## Hugging Face Setup

1. Get your token from: https://huggingface.co/settings/tokens
2. Accept model agreements:
   - https://huggingface.co/pyannote/speaker-diarization-3.1
   - https://huggingface.co/pyannote/segmentation-3.0

## Processing Time

With CUDA GPU (RTX 5070):
- ~45 minutes for a 60-minute audio file

Without GPU (CPU only):
- Several hours for a 60-minute audio file

## File Locations

- `setup_env.sh` - Your personal environment setup (gitignored)
- `setup_env.sh.example` - Template for new users
- `diarize_and_combine.py` - Main transcription script
- `venv/` - Python virtual environment (gitignored)

## Security Note

Never commit `setup_env.sh` with your actual token. It's automatically ignored by git.
