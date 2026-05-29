import sys
import os

# Add scripts directory to path
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from process_single_post_process import validate_output_quality

def test_quality_validation():
    input_text = """**[00:01] SPEAKER_00:** Welcome to the Ethereum podcast. We are discussing NFTs and Solidity today with Vitalik Buterin and Kieren James-Lubin.

    **[00:15] SPEAKER_01:** Yes, the EVM and ZK-rollups are very important for scalability."""

    # Case 1: Good output
    output_good = """**[00:01] SPEAKER_00:** Welcome to the Ethereum podcast. We are discussing NFTs and Solidity today with Vitalik Buterin and Kieren James-Lubin.

    **[00:15] SPEAKER_01:** Yes, the EVM and ZK-rollups are very important for scalability."""

    # Case 2: Missing technical terms (hallucination or aggressive cleanup)
    output_bad_terms = """**[00:01] SPEAKER_00:** Welcome to the podcast. We are discussing digital art and coding today with some experts.

    **[00:15] SPEAKER_01:** Yes, scaling is very important."""

    # Case 3: Missing names
    output_bad_names = """**[00:01] SPEAKER_00:** Welcome to the Ethereum podcast. We are discussing NFTs and Solidity today with some guys.

    **[00:15] SPEAKER_01:** Yes, the EVM and ZK-rollups are very important for scalability."""

    print("Testing quality validation...")

    v1, issues1 = validate_output_quality(input_text, output_good, "opus")
    print(f"Good output: Valid={v1}, Issues={issues1}")

    v2, issues2 = validate_output_quality(input_text, output_bad_terms, "opus")
    print(f"Bad terms: Valid={v2}, Issues={issues2}")

    v3, issues3 = validate_output_quality(input_text, output_bad_names, "opus")
    print(f"Bad names: Valid={v3}, Issues={issues3}")

if __name__ == "__main__":
    test_quality_validation()
