#!/usr/bin/env python3
"""
AssemblyAI transcription alternative to WhisperX
Uses AssemblyAI's cloud transcription with speaker diarization
No file size limits, excellent diarization, cost-effective
"""

import os
import sys
from pathlib import Path
import argparse
import time

def transcribe_with_assemblyai(audio_path, output_dir="intermediates"):
    """
    Transcribe audio using AssemblyAI with speaker diarization
    
    Args:
        audio_path: Path to audio file
        output_dir: Where to save transcript
    
    Returns:
        path to transcript file
    """
    try:
        import assemblyai as aai
    except ImportError:
        print("Error: assemblyai package not installed")
        print("Install with: pip install assemblyai")
        sys.exit(1)
    
    api_key = os.environ.get('ASSEMBLYAI_API_KEY')
    if not api_key:
        print("Error: ASSEMBLYAI_API_KEY not set")
        print("Set it with: export ASSEMBLYAI_API_KEY='your-key'")
        print("Get key from: https://www.assemblyai.com/")
        sys.exit(1)
    
    aai.settings.api_key = api_key
    audio_file_path = Path(audio_path)
    
    if not audio_file_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    file_size_mb = audio_file_path.stat().st_size / 1024 / 1024
    
    print("="*70)
    print("AssemblyAI Transcription with Speaker Diarization")
    print("="*70)
    print(f"Input: {audio_path}")
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"Features: Speaker diarization, timestamps")
    print()
    
    print("Uploading and transcribing...")
    print("(AssemblyAI processes asynchronously - this may take several minutes)")
    print()
    
    # Configure transcription with speaker diarization
    config = aai.TranscriptionConfig(
        speaker_labels=True,  # Enable speaker diarization
        speakers_expected=None  # Auto-detect number of speakers
    )
    
    transcriber = aai.Transcriber()
    
    # Start transcription (async)
    print("→ Uploading file...")
    transcript = transcriber.transcribe(str(audio_file_path), config=config)
    
    # Poll for completion
    print("→ Processing (checking status every 5 seconds)...")
    while transcript.status not in [aai.TranscriptStatus.completed, aai.TranscriptStatus.error]:
        time.sleep(5)
        print("  ⋯ Still processing...")
    
    if transcript.status == aai.TranscriptStatus.error:
        print(f"\n❌ Error: {transcript.error}")
        sys.exit(1)
    
    print("✓ Transcription complete")
    print()
    
    # Format output to match WhisperX style
    formatted_lines = []
    
    if transcript.utterances:
        # Use utterances (grouped by speaker)
        for utterance in transcript.utterances:
            # Convert milliseconds to seconds
            start_time = utterance.start / 1000.0
            # Map speaker (A, B, C...) to WhisperX format (SPEAKER_00, SPEAKER_01...)
            speaker_num = ord(utterance.speaker) - ord('A')
            speaker_label = f"SPEAKER_{speaker_num:02d}"
            text = utterance.text.strip()
            
            formatted_lines.append(f"[{start_time:.1f}s] {speaker_label}: {text}")
    else:
        # Fallback to full text if no utterances
        formatted_lines.append(f"[0.0s] SPEAKER_00: {transcript.text}")
    
    formatted = '\n'.join(formatted_lines)
    
    # Save to intermediates/ with _assemblyai suffix
    original_stem = Path(audio_path).stem
    output_path = Path(output_dir) / f"{original_stem}_assemblyai_transcript_with_speakers.txt"
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted)
    
    # Also save markdown version
    md_path = output_path.with_suffix('.md')
    md_content = formatted.replace('SPEAKER_', '**SPEAKER_').replace(': ', ':** ')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Saved transcript: {output_path}")
    print(f"Saved markdown: {md_path}")
    print()
    
    # Stats
    char_count = len(formatted)
    line_count = len(formatted_lines)
    num_speakers = len(set(utterance.speaker for utterance in transcript.utterances)) if transcript.utterances else 1
    
    print("Transcript stats:")
    print(f"  Lines: {line_count}")
    print(f"  Characters: {char_count}")
    print(f"  Speakers detected: {num_speakers}")
    print(f"  Duration: {transcript.audio_duration / 1000.0 / 60:.1f} minutes")
    
    # Cost estimate
    duration_minutes = transcript.audio_duration / 1000.0 / 60
    estimated_cost = duration_minutes * 0.015  # ~$0.015/minute
    print(f"  Estimated cost: ${estimated_cost:.2f}")
    print()
    
    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio using AssemblyAI with speaker diarization",
        epilog="""
Example:
  python3 transcribe_with_assemblyai.py audio.mp3
  
Features:
  - No file size limits (unlike OpenAI's 25MB limit)
  - Built-in speaker diarization
  - Cost-effective (~$0.01-0.02 per minute)
  
Setup:
  1. Get API key from https://www.assemblyai.com/
  2. Set environment variable:
     export ASSEMBLYAI_API_KEY='your-key'
  3. Install SDK:
     pip install assemblyai
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("audio", help="Path to audio file (MP3, WAV, etc.)")
    parser.add_argument("--output-dir", default="intermediates",
                       help="Output directory (default: intermediates)")
    
    args = parser.parse_args()
    
    try:
        output_path = transcribe_with_assemblyai(args.audio, args.output_dir)
        
        print("="*70)
        print("✓ Transcription complete!")
        print("="*70)
        print()
        print("Next steps:")
        print("  1. Review the transcript")
        print("  2. Post-process with AI:")
        print(f"     python3 scripts/post_process_transcript.py {output_path} --provider openai")
        print()
        
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
