"""Entropy calculation for SOC File Forensics Analyzer."""
import math


def shannon_entropy(file_path: str) -> float:
    """Calculate the Shannon entropy of a file.

    High entropy can indicate packed or encrypted data.

    Args:
        file_path: Path to the file to analyze.

    Returns:
        Entropy value (bits per byte).
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except Exception as e:
        raise IOError(f"Could not read file for entropy calculation: {e}")

    if not data:
        return 0.0

    # frequency of each byte value
    freq = [0] * 256
    for byte in data:
        freq[byte] += 1

    entropy = 0.0
    length = len(data)

    for count in freq:
        if count == 0:
            continue
        p = count / length
        entropy -= p * math.log2(p)

    return entropy
