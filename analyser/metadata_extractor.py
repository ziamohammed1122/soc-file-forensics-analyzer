"""Metadata extraction utilities for SOC File Forensics Analyzer."""
import os
import datetime


def extract_metadata(file_path: str) -> dict:
    """Extract basic metadata from a file.

    Args:
        file_path: Path to the file to inspect.

    Returns:
        Dictionary with keys 'size', 'created', 'modified'.
    """
    try:
        stats = os.stat(file_path)
    except Exception as e:
        raise IOError(f"Could not access file metadata: {e}")

    size = stats.st_size
    created = datetime.datetime.fromtimestamp(stats.st_ctime)
    modified = datetime.datetime.fromtimestamp(stats.st_mtime)

    return {
        'size': size,
        'created': created.isoformat(),
        'modified': modified.isoformat(),
    }
