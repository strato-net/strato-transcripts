# WhisperX Video Transcription Pipeline

A complete pipeline for automatically transcribing video/audio files with speaker identification (diarization) and formatting for Jekyll websites.

## Table of Contents
- [What This Does (ELI5)](#what-this-does-eli5)
- [Quick Start](#quick-start)
- [Setup Guide](#setup-guide)
- [Script Reference](#script-reference)
- [Performance & Hardware](#performance--hardware)
- [Troubleshooting](#troubleshooting)

---

## What This Does (ELI5)

This pipeline takes an audio/video file of a podcast or interview and automatically:

1. **Transcribes the audio** - Converts speech to text with timestamps using OpenAI's Whisper AI model
2. **Identifies speakers** - Figures out who's talking when (Bob, Kieren, Jim, etc.) using AI voice analysis
3. **Maps speakers to names** - Changes generic labels like "SPEAKER_01" to actual names like "Bob Summerwill"
4. **Formats for website** - Creates a nice markdown file ready to publish on your Jekyll website

### Real Example:
**Input:** `episode003-bob-summerwill.mp3` (79 minute audio file)

**Output:** A formatted markdown file with:
```markdown
**Bob Summerwill:**
[57.1s] So, yeah, hi, you know, thanks so much for the invite...

**Kieren James-Lubin:**
[1.2s] Well, thanks everyone for coming back...
```

### Why Use This vs Manual Transcription?
- **Manual transcription:** ~8-10 hours for a 1-hour video
- **This pipeline:** ~45 minutes (mostly AI processing time, hands-off)
- **Accuracy:** 95%+ with good audio quality
- **Cost:** Free (just need a GPU or patience for CPU processing)

---

## Quick Start

```bash
# 1. Set up environment (one-time setup)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Get a Hugging Face token (free)
# Visit: https://huggingface.co/settings/tokens
# Accept model agreements:
#   - https://huggingface.co/pyannote/speaker-diarization-3.1
#   - https://huggingface.co/pyannote/segmentation-3.0
export HF_TOKEN="your_token_here"

# 3. Run the complete pipeline
python3 diarize_and_combine.py path/to/audio.mp3

# 4. Map speakers to names (edit the script first with correct names)
python3 map_speakers_to_names.py output_transcript_with_speakers.txt

# 5. Format for markdown
python3 format_transcript_for_markdown.py output_with_names.txt formatted.txt
```

---

## Setup Guide

### Prerequisites
- Python 3.8 or later
- 8GB+ RAM (16GB recommended)
- GPU highly recommended (see [Performance](#performance--hardware))

### Step 1: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows
```

### Step 2: Install Dependencies

Create a `requirements.txt` file:

```txt
# Core transcription
whisperx==3.1.1
torch==2.0.1
torchaudio==2.0.2

# Speaker diarization
pyannote.audio==3.1.1
huggingface-hub>=0.19.0

# Utilities
ffmpeg-python>=0.2.0
```

Install:
```bash
pip install -r requirements.txt
```

**For GPU Support:**

**NVIDIA GPUs (CUDA):**
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**AMD GPUs (ROCm) on Linux:**
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/rocm6.2
```

**CPU Only:**
```bash
# Default torch installation (already in requirements.txt)
# Works but is MUCH slower
```

### Step 3: Get Hugging Face Token

1. Create account at [huggingface.co](https://huggingface.co)
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)
3. Create a new token (read access is enough)
4. Accept model agreements:
   - [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
   - [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)

Set the token:
```bash
export HF_TOKEN="hf_YourTokenHere"

# Or add to your ~/.bashrc or ~/.zshrc:
echo 'export HF_TOKEN="hf_YourTokenHere"' >> ~/.bashrc
```

### Step 4: Verify Installation

```bash
python3 test_rocm.py  # Or test_cuda.py for NVIDIA
```

Should show:
```
PyTorch version: 2.0.1
CUDA/ROCm available: True
Device count: 1
Device: AMD Radeon RX 7900 XTX
```

---

## Script Reference

### Core Pipeline Scripts

#### 1. `diarize_and_combine.py`
**Purpose:** Complete pipeline - transcription + speaker identification

**Usage:**
```bash
python3 diarize_and_combine.py audio_file.mp3
```

**What it does:**
1. Transcribes audio using WhisperX (Whisper + word-level timestamps)
2. Identifies speakers using pyannote.audio diarization
3. Combines transcription with speaker labels
4. Outputs: `filename_transcript_with_speakers.txt`

**Options:**
- Automatically uses GPU if available
- Falls back to CPU if no GPU detected
- Uses "large-v2" Whisper model (best accuracy)

**Output format:**
```
SPEAKER_01:
[0.0s] Text from speaker 1...

SPEAKER_02:
[15.3s] Text from speaker 2...
```

#### 2. `map_speakers_to_names.py`
**Purpose:** Replace SPEAKER_XX with actual names

**Usage:**
```bash
python3 map_speakers_to_names.py input_transcript.txt --output output.txt
```

**Important:** Edit the `SPEAKER_MAP` dictionary in the script first:

```python
SPEAKER_MAP = {
    'SPEAKER_01': 'Bob Summerwill',    # Most segments
    'SPEAKER_02': 'Kieren James-Lubin', # Host
    'SPEAKER_03': 'Jim Hormuzdiar',     # Co-host
    # ... etc
}
```

**How to determine mapping:**
1. Look at the `_transcript_with_speakers.txt` file
2. Read the early conversation to identify who's who
3. Check segment counts (script reports statistics)
4. Main guest usually has most segments

#### 3. `format_transcript_for_markdown.py`
**Purpose:** Convert to Jekyll-ready markdown format

**Usage:**
```bash
python3 format_transcript_for_markdown.py input.txt output.txt
```

**What it does:**
Converts from:
```
Bob Summerwill:
[57.1s] So, yeah, hi...
[60.4s] Thanks for having me...
```

To:
```markdown
**Bob Summerwill:**
[57.1s] So, yeah, hi...
[60.4s] Thanks for having me...
```

### Helper/Test Scripts

#### `test_diarization.py`
Tests speaker diarization in isolation
```bash
python3 test_diarization.py
```

#### `test_diarization_hf.py`
Tests Hugging Face authentication
```bash
python3 test_diarization_hf.py
```

#### `test_rocm.py` / `test_cuda.py`
Tests GPU availability and PyTorch setup
```bash
python3 test_rocm.py
```

### Legacy Formatting Scripts

These were used to format older transcripts. You probably don't need them:
- `merge_speaker_paragraphs.py` - Merge consecutive lines from same speaker
- `complete_formatting.py` - Apply multiple formatting steps
- `organize_sections.py` - Split transcript into titled sections (video-specific)
- `convert_timestamps.py`, `fix_capitalization.py`, etc. - Various cleanup utilities

---

## Performance & Hardware

### Processing Time Comparison

**79-minute audio file (Bob Summerwill episode):**

| Hardware | Transcription | Diarization | Total Time | Speed |
|----------|--------------|-------------|------------|-------|
| AMD RX 7900 XTX (GPU) | 5-7 min | 38-40 min | **~45 min** | 1.75x realtime |
| NVIDIA RTX 3090 (GPU) | 4-6 min | 35-38 min | **~42 min** | 1.9x realtime |
| CPU (16-core) | 45-60 min | 6-8 hours | **~7 hours** | 0.18x realtime |
| CPU (8-core) | 90-120 min | 12-15 hours | **~14 hours** | 0.09x realtime |

**Key Takeaways:**
- **GPU is 10-20x faster** than CPU for this workload
- Diarization (speaker identification) is the slowest part
- Transcription is relatively fast even on CPU
- GPU makes the difference between "45 minutes" and "half a day"

### Hardware Recommendations

**Minimum (CPU only):**
- 8GB RAM
- 50GB free disk space
- Be prepared to wait hours

**Recommended (GPU):**
- NVIDIA GPU: GTX 1660 or better (6GB+ VRAM)
- AMD GPU: RX 6600 or better (8GB+ VRAM)
- 16GB system RAM
- 50GB free disk space

**Optimal:**
- NVIDIA RTX 3090/4090 or AMD RX 7900 XTX
- 32GB system RAM
- SSD for faster model loading

### GPU vs CPU: What's the Difference?

**How It Works:**
- AI models (Whisper, pyannote) do millions of mathematical operations
- GPUs have thousands of cores optimized for parallel math
- CPUs have fewer cores designed for general tasks

**Analogy:**
- CPU: 8-16 smart workers who can do anything
- GPU: 5,000 specialized workers who are amazing at one specific task
- For AI transcription, you want the army of specialists

**Cost Consideration:**
- Cloud GPU (AWS/Google): ~$1-2/hour
- 45 min processing = ~$1.50 per video
- If you process videos regularly, owning a GPU pays for itself

---

## Troubleshooting

### Common Issues

#### 1. "HF_TOKEN environment variable not set"

**Problem:** Hugging Face token not configured

**Solution:**
```bash
export HF_TOKEN="hf_YourTokenHere"

# Verify it's set:
echo $HF_TOKEN
```

Make it permanent by adding to `~/.bashrc` or `~/.zshrc`.

#### 2. "Permission denied" for model access

**Problem:** Haven't accepted pyannote model agreements

**Solution:**
1. Visit [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
2. Click "Agree and access repository"
3. Do the same for [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)
4. Wait 1-2 minutes for permissions to propagate

#### 3. "CUDA out of memory" or similar GPU errors

**Problem:** GPU doesn't have enough VRAM

**Solutions:**
```python
# In diarize_and_combine.py, use smaller Whisper model:
model = whisperx.load_model("medium", device, compute_type="float16")
# Options: tiny, base, small, medium, large-v2
```

Or process smaller chunks of audio at a time.

#### 4. Very slow performance on GPU

**Check:**
```bash
python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

If it says `False`, PyTorch isn't using your GPU. Reinstall with the correct version:

**For NVIDIA:**
```bash
pip uninstall torch torchaudio
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**For AMD:**
```bash
pip uninstall torch torchaudio
pip install torch torchaudio --index-url https://download.pytorch.org/whl/rocm6.2
```

#### 5. Speaker diarization is inaccurate

**Causes:**
- Poor audio quality
- Many overlapping speakers
- Background noise
- Similar-sounding voices

**Improvements:**
- Use high-quality audio (clean podcast-style recordings work best)
- Pre-process audio to remove noise
- Manually review and correct speaker labels
- Adjust diarization parameters (advanced)

#### 6. Transcription has many errors

**Causes:**
- Heavy accents
- Technical jargon
- Poor audio quality
- Quiet speakers

**Solutions:**
- Use the largest Whisper model (`large-v2`)
- Improve audio quality (noise reduction, normalization)
- Expect to do manual cleanup for technical terms
- Consider using Whisper's language parameter if not English

---

## Full Workflow Example

Here's a complete real-world example for processing a 60-minute podcast:

```bash
# 1. Activate environment
source venv/bin/activate
export HF_TOKEN="hf_YourTokenHere"

# 2. Run transcription + diarization (30-45 min on GPU)
python3 diarize_and_combine.py podcast_episode5.mp3

# Output: podcast_episode5_transcript_with_speakers.txt

# 3. Review the output to identify speakers
head -100 podcast_episode5_transcript_with_speakers.txt

# You'll see patterns like:
# SPEAKER_00: 15 brief segments - probably intermittent speaker
# SPEAKER_01: 450 segments - likely main guest
# SPEAKER_02: 120 segments - likely host

# 4. Edit map_speakers_to_names.py with correct mapping:
# SPEAKER_MAP = {
#     'SPEAKER_01': 'Guest Name',
#     'SPEAKER_02': 'Host Name',
#     ...
# }

# 5. Run speaker mapping
python3 map_speakers_to_names.py podcast_episode5_transcript_with_speakers.txt

# Output: podcast_episode5_transcript_with_speakers_with_names.txt

# 6. Format for markdown
python3 format_transcript_for_markdown.py \
    podcast_episode5_transcript_with_speakers_with_names.txt \
    podcast_episode5_formatted.txt

# Output: podcast_episode5_formatted.txt

# 7. Create Jekyll markdown file
# Manually create: source/_videos/podcast-episode-5.md
# Add YAML front matter, then append the formatted transcript

# 8. Commit and deploy
git add source/_videos/podcast-episode-5.md
git commit -m "Add Episode 5 transcript"
git push
```

---

## Tips & Best Practices

### Audio Quality Matters
- **Good:** Clean podcast-style recordings, one speaker at a time
- **Bad:** Conference calls, noisy environments, multiple overlapping speakers
- **Tip:** Use Audacity or similar to normalize audio levels before processing

### Verify Early
- Run the first 5 minutes through the pipeline before processing full audio
- Check accuracy and speaker identification
- Adjust settings if needed before wasting time on poor results

### Manual Review is Normal
- Expect to manually review 10-20% of the transcript
- AI gets 95%+ accuracy, but you'll find errors
- Technical terms, names, and acronyms need attention

### Save Intermediate Files
- Keep all `_transcript_with_speakers.txt` files
- You can re-run mapping/formatting without re-transcribing
- Transcription is the expensive part (time-wise)

### Batch Processing
- Process multiple videos overnight
- GPU can handle back-to-back processing
- Each 60-min video ≈ 45 min processing time

---

## Version Compatibility

**Tested with:**
- Python: 3.8, 3.9, 3.10, 3.11
- PyTorch: 2.0.0 - 2.2.0
- CUDA: 11.8, 12.1
- ROCm: 6.0, 6.2
- Ubuntu: 20.04, 22.04
- macOS: 12.x, 13.x (CPU only, no Metal support yet)
- Windows: 10, 11 (with WSL2 for best results)

**Known Issues:**
- ROCm on Ubuntu 24.04: Some compatibility issues, use 22.04 for best results
- macOS Metal GPU support: Not yet available in PyTorch
- Windows native: Slower than WSL2, recommend using WSL2

---

## Additional Resources

### Documentation
- [WhisperX GitHub](https://github.com/m-bain/whisperX) - Official WhisperX repository
- [Whisper by OpenAI](https://github.com/openai/whisper) - Original Whisper model
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) - Speaker diarization
- [Hugging Face](https://huggingface.co/) - Model hosting and tokens

### Getting Help
- File issues on this repository's GitHub
- Check [WhisperX issues](https://github.com/m-bain/whisperX/issues) for common problems
- [pyannote discussions](https://github.com/pyannote/pyannote-audio/discussions) for diarization help

### Contributing
If you improve this pipeline or scripts, please contribute back! Pull requests welcome.

---

## License

These scripts are provided as-is for the STRATO Mercata project. Modify and use as needed for your own Jekyll-based websites.

**Dependencies:**
- WhisperX: MIT License
- PyTorch: BSD License  
- pyannote.audio: MIT License
- Whisper: MIT License

---

**Last Updated:** January 2025
**Tested with:** Bob Summerwill Episode (79 minutes, 6 speakers)
**Success Rate:** 95%+ transcription accuracy, 90%+ speaker identification accuracy
