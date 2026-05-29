import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from common import save_transcript_dual_format

def test_save_transcript_robustness():
    output_dir = "tests/output"
    basename = "test_episode"
    service_name = "whisperx"

    # Case 1: Missing speaker or text or start in segments
    segments = [
        {"start": 1.0, "text": "Hello", "speaker": "SPEAKER_01"},
        {"start": 2.0, "text": "World"}, # Missing speaker
        {"start": 3.0, "speaker": "SPEAKER_02"}, # Missing text
        {"text": "No start", "speaker": "SPEAKER_01"} # Missing start
    ]

    print("Testing save_transcript_dual_format with malformed segments...")
    try:
        md_path = save_transcript_dual_format(output_dir, basename, service_name, segments, content_type="segments")
        print(f"PASS: Function returned {md_path}")
        if md_path.exists():
            with open(md_path, 'r') as f:
                content = f.read()
                print("Content of generated MD:")
                print(content)
    except Exception as e:
        print(f"FAIL: Function raised exception: {e}")

if __name__ == "__main__":
    test_save_transcript_robustness()
