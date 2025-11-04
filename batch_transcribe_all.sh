#!/bin/bash
# Batch transcribe all MP3 files and collect timing data

set -e

# Setup environment
source setup_env.sh
source venv/bin/activate
export LD_LIBRARY_PATH=venv/lib/python3.12/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH

# Output file for results
RESULTS_FILE="transcription_results.csv"
echo "filename,audio_duration_min,transcription_sec,diarization_sec,assignment_sec,total_sec,speakers" > "$RESULTS_FILE"

# Directory containing MP3 files
AUDIO_DIR="source/videos/raw-audio"

# Counter
count=0
total_files=$(ls -1 "$AUDIO_DIR"/*.mp3 | wc -l)

echo "=================================================="
echo "Batch Transcription Pipeline"
echo "=================================================="
echo "Total files to process: $total_files"
echo "Estimated time: $(echo "$total_files * 5" | bc) minutes"
echo "=================================================="
echo ""

# Process each MP3 file
for mp3_file in "$AUDIO_DIR"/*.mp3; do
    # Skip if transcript already exists
    base_name=$(basename "$mp3_file" .mp3)
    transcript_file="${AUDIO_DIR}/${base_name}_transcript_with_speakers.txt"
    
    count=$((count + 1))
    
    echo ""
    echo "=================================================="
    echo "[$count/$total_files] Processing: $base_name"
    echo "=================================================="
    
    # Get audio duration using ffprobe
    duration_sec=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$mp3_file" 2>/dev/null || echo "0")
    duration_min=$(echo "scale=1; $duration_sec / 60" | bc)
    
    echo "Audio duration: ${duration_min} minutes"
    
    # Run transcription and capture output
    start_time=$(date +%s)
    output=$(python3 transcribe_with_diarization.py "$mp3_file" 2>&1)
    end_time=$(date +%s)
    total_time=$((end_time - start_time))
    
    # Parse output for timing data
    transcription_time=$(echo "$output" | grep "Transcription complete in" | sed 's/.*in \([0-9.]*\)s.*/\1/' || echo "0")
    diarization_time=$(echo "$output" | grep "Diarization complete in" | sed 's/.*in \([0-9.]*\)s.*/\1/' || echo "0")
    
    # Extract number of speakers
    speakers=$(echo "$output" | grep "Detected .* speakers" | sed 's/.*Detected \([0-9]*\) speakers.*/\1/' || echo "0")
    
    # Calculate assignment time (total - transcription - diarization)
    assignment_time=$(echo "$total_time - $transcription_time - $diarization_time" | bc)
    
    # Save to CSV
    echo "$base_name,$duration_min,$transcription_time,$diarization_time,$assignment_time,$total_time,$speakers" >> "$RESULTS_FILE"
    
    echo "✓ Complete: ${total_time}s total"
    echo "  - Transcription: ${transcription_time}s"
    echo "  - Diarization: ${diarization_time}s"
    echo "  - Assignment: ${assignment_time}s"
    echo "  - Speakers: $speakers"
done

echo ""
echo "=================================================="
echo "All files processed successfully!"
echo "Results saved to: $RESULTS_FILE"
echo "=================================================="

# Generate summary table
python3 << 'PYTHON_SCRIPT'
import pandas as pd
import sys

# Read results
df = pd.read_csv('transcription_results.csv')

# Calculate totals
total_audio = df['audio_duration_min'].sum()
total_transcription = df['transcription_sec'].sum()
total_diarization = df['diarization_sec'].sum()
total_assignment = df['assignment_sec'].sum()
total_time = df['total_sec'].sum()

print("\n" + "="*80)
print("TRANSCRIPTION SUMMARY - RTX 5070")
print("="*80)
print(f"\nFiles processed: {len(df)}")
print(f"Total audio duration: {total_audio:.1f} minutes ({total_audio/60:.1f} hours)")
print(f"\nTotal processing time: {total_time:.0f} seconds ({total_time/60:.1f} minutes)")
print(f"  - Transcription: {total_transcription:.0f}s ({total_transcription/60:.1f} min)")
print(f"  - Diarization: {total_diarization:.0f}s ({total_diarization/60:.1f} min)")
print(f"  - Assignment: {total_assignment:.0f}s ({total_assignment/60:.1f} min)")

print(f"\nAverage speed: {total_audio / (total_time/60):.1f}x realtime")
print(f"Minutes of audio per minute of processing: {total_audio / (total_time/60):.1f}x")

print("\n" + "="*80)
print("PER-FILE BREAKDOWN")
print("="*80)
print(f"\n{'Filename':<45} {'Audio':>7} {'Trans':>7} {'Diar':>7} {'Total':>7} {'Spk':>4}")
print(f"{'':45} {'(min)':>7} {'(sec)':>7} {'(sec)':>7} {'(sec)':>7} {'':>4}")
print("-"*80)

for _, row in df.iterrows():
    print(f"{row['filename']:<45} {row['audio_duration_min']:>7.1f} {row['transcription_sec']:>7.0f} {row['diarization_sec']:>7.0f} {row['total_sec']:>7.0f} {row['speakers']:>4.0f}")

print("-"*80)
print(f"{'TOTAL':<45} {total_audio:>7.1f} {total_transcription:>7.0f} {total_diarization:>7.0f} {total_time:>7.0f}")
print("="*80)

# Calculate estimated manual transcription time
manual_hours = total_audio / 60 * 10  # 10:1 ratio for manual
print(f"\nEstimated manual transcription time: {manual_hours:.1f} hours")
print(f"Time saved vs manual: {manual_hours - (total_time/3600):.1f} hours")
print(f"Speed improvement: {manual_hours / (total_time/3600):.0f}x faster")
print("="*80)

PYTHON_SCRIPT

echo ""
echo "Done!"
