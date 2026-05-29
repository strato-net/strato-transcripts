import sys
import os

# Add scripts directory to path so we can import from it
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from process_single_post_process import strip_ai_preamble

def test_strip_ai_preamble():
    test_cases = [
        {
            "name": "Standard bold with timestamp",
            "input": "Here is the transcript:\n\n**[00:01] SPEAKER_00:** Hello world.",
            "expected_start": "**[00:01] SPEAKER_00:** Hello world."
        },
        {
            "name": "No bold with timestamp",
            "input": "Thinking: I should process this.\n[00:01] SPEAKER_00: Hello world.",
            "expected_start": "[00:01] SPEAKER_00: Hello world."
        },
        {
            "name": "Multiple thinking blocks (o1 style)",
            "input": "> I will now clean up the transcript.\n> I will preserve all timestamps.\n\n**[00:01] SPEAKER_00:** Hello world.",
            "expected_start": "**[00:01] SPEAKER_00:** Hello world."
        },
        {
            "name": "Gemini style preamble",
            "input": "The following is a cleaned version of the transcript provided, with technical terms corrected and speaker labels preserved.\n\n**[00:01] SPEAKER_00:** Hello world.",
            "expected_start": "**[00:01] SPEAKER_00:** Hello world."
        },
        {
            "name": "Markdown code block wrap",
            "input": "```markdown\n**[00:01] SPEAKER_00:** Hello world.\n```",
            "expected_start": "**[00:01] SPEAKER_00:** Hello world."
        },
        {
            "name": "Edge case: Lowercase speaker",
            "input": "Preamble here.\n**[00:01] speaker_00:** Hello world.",
            "expected_start": "**[00:01] speaker_00:** Hello world."
        },
        {
            "name": "Edge case: Extra spaces",
            "input": "Preamble here.\n** [00:01]   SPEAKER_00 : ** Hello world.",
            "expected_start": "** [00:01]   SPEAKER_00 : ** Hello world."
        }
    ]

    passed = 0
    for case in test_cases:
        result = strip_ai_preamble(case["input"]).strip()
        # Clean up expected if it's wrapped in markdown for the test
        expected = case["expected_start"].strip()

        if result.startswith(expected):
            print(f"PASS: {case['name']}")
            passed += 1
        else:
            print(f"FAIL: {case['name']}")
            print(f"  Expected start: {expected[:50]}...")
            print(f"  Actual start:   {result[:50]}...")

    print(f"\nPassed {passed}/{len(test_cases)}")

if __name__ == "__main__":
    test_strip_ai_preamble()
