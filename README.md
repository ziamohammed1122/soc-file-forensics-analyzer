# soc-file-forensics-analyzer

A Python-based tool for Security Operations Center (SOC) analysts and digital forensics investigators. The project helps analyze suspicious files using hashing, entropy analysis, metadata extraction, and machine learning-based malware detection.

## Features

- Generate MD5, SHA1, and SHA256 hashes for files
- Calculate Shannon entropy to flag packed/encrypted files
- Extract basic file metadata (size, creation/modification times)
- Machine learning classification (Random Forest) to label files as SAFE or MALICIOUS

## Installation

```bash
# clone the repository
git clone https://github.com/username/soc-file-forensics-analyzer.git
cd soc-file-forensics-analyzer

# create a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # on Linux

# install dependencies
pip install -r requirements.txt
```

## Linux Setup

This project is designed to run on Linux systems. Ensure you have Python 3.7+ installed. The commands above assume a Bash-compatible shell.

## Usage

### Train the ML model

```bash
python3 models/train_model.py
```

This script reads `dataset/malware_dataset.csv`, trains a Random Forest classifier, prints a classification report, and saves the model to `models/random_forest_model.joblib`.

### Run the analyzer

```bash
python3 analyzer/main.py <path_to_file>
```

You may specify multiple files at once:

```bash
python3 analyzer/main.py suspicious.exe another.bin
```

## Example Output

```
Analyzing: suspicious.exe

-- Metadata --
Size: 54321
Created: 2023-01-01T12:34:56
Modified: 2023-01-02T08:00:00

-- Hashes --
MD5: d41d8cd98f00b204e9800998ecf8427e
SHA1: da39a3ee5e6b4b0d3255bfef95601890afd80709
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Entropy: 7.5231

Final classification: MALICIOUS
```

## Future Improvements

- Expand dataset and feature set (e.g., entropy of sections, imports)
- Integrate with YARA or VirusTotal APIs
- Add GUI or web interface for analysts
- Support batch scanning and report generation

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

