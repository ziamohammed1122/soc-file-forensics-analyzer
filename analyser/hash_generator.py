"""Hash generation utilities for SOC File Forensics Analyzer."""
import hashlib


def compute_hashes(file_path: str) -> dict:
    """Compute MD5, SHA1, and SHA256 hashes for a given file.

    Args:
        file_path: Path to the file to hash.

    Returns:
        Dictionary with keys 'md5', 'sha1', 'sha256'.
    """
    hashes = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha256': hashlib.sha256(),
    }

    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                for h in hashes.values():
                    h.update(chunk)
    except Exception as e:
        raise IOError(f"Could not read file for hashing: {e}")

    return {name: h.hexdigest() for name, h in hashes.items()}
