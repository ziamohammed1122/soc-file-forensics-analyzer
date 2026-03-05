"""Main entry point for SOC File Forensics Analyzer."""
import argparse
import sys
# absolute imports ensure the module can be executed as a script
from analyzer.hash_generator import compute_hashes
from analyzer.entropy_analyzer import shannon_entropy
from analyzer.metadata_extractor import extract_metadata
from analyzer.ml_detector import predict


def analyze_file(file_path: str):
    print(f"Analyzing: {file_path}")
    try:
        meta = extract_metadata(file_path)
        hashes = compute_hashes(file_path)
        entropy = shannon_entropy(file_path)
    except Exception as e:
        print(f"Error processing file: {e}")
        return

    print("\n-- Metadata --")
    for k, v in meta.items():
        print(f"{k.capitalize()}: {v}")

    print("\n-- Hashes --")
    for k, v in hashes.items():
        print(f"{k.upper()}: {v}")

    print(f"\nEntropy: {entropy:.4f}")

    features = {'size': meta['size'], 'entropy': entropy}
    try:
        classification = predict(features)
    except Exception as e:
        print(f"Model error: {e}")
        classification = "UNKNOWN"

    print(f"\nFinal classification: {classification}")


def main():
    parser = argparse.ArgumentParser(description="SOC File Forensics Analyzer")
    parser.add_argument('files', nargs='+', help='Path(s) to file(s) to analyze')
    args = parser.parse_args()

    for f in args.files:
        analyze_file(f)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No file specified. Use -h for help.")
    main()
