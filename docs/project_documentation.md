# Project Documentation

## System Architecture

The repository is structured into four main directories:

- `dataset/`: contains CSV files used for training the ML model.
- `analyzer/`: core Python modules that implement hashing, entropy calculation, metadata extraction, and classification logic, plus the `main.py` entry point.
- `models/`: training script and serialized model artifacts.
- `docs/`: additional documentation (this file).

Modules are intentionally small and focused, allowing for easy testing and reuse.

## Machine Learning Workflow

1. **Data Collection**: A labeled CSV (`dataset/malware_dataset.csv`) holds features such as file size, hashes, entropy, and a binary label (0=safe, 1=malware).
2. **Feature Selection**: For the demonstration, only `file_size` and `entropy` are used. Additional columns (hashes) are preserved for completeness but not fed into the model.
3. **Training**: `models/train_model.py` loads the dataset, splits into training/testing subsets, and trains a `RandomForestClassifier` from `scikit-learn`.
4. **Evaluation**: After training, the script prints a classification report (precision/recall/f1-score) on the test set and saves the model using `joblib`.
5. **Deployment**: The analyzer uses the saved model to score new files via `analyzer/ml_detector.py`.

## Feature Extraction

Before classification, each file is processed by the following steps:

1. **Metadata Extraction** (`metadata_extractor.py`): Records size, creation/modification timestamps.
2. **Hash Generation** (`hash_generator.py`): Computes MD5, SHA1, and SHA256 for triage and sharing.
3. **Entropy Calculation** (`entropy_analyzer.py`): Determines Shannon entropy to highlight compressed or encrypted payloads.

These values are displayed to the analyst and used by the ML model.

## SOC Investigation Use Case

A SOC analyst receives a suspicious binary from an endpoint detection system. Running the analyzer yields a quick summary of the file's properties and an automated prediction. The hashes can be cross-referenced with threat intelligence, the entropy may indicate packing, and the ML label provides a baseline assessment. This lightweight tool is intended to augment existing workflows and serve as a teaching aid in forensic training.
