"""Machine learning malware detection using a pre-trained model."""
import os
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'random_forest_model.joblib')


def load_model(path: str = MODEL_PATH):
    """Load the trained ML model from disk."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}. Please train the model first.")
    return joblib.load(path)


def predict(file_features: dict, model=None) -> str:
    """Predict whether a file is SAFE or MALICIOUS using its features.

    Args:
        file_features: dict containing numeric features used in training (e.g. size, entropy).
        model: optional pre-loaded sklearn model; if None, the default model is loaded.

    Returns:
        'SAFE' or 'MALICIOUS'.
    """
    if model is None:
        model = load_model()

    # prepare feature vector as list of values in consistent order
    # our training uses ['file_size', 'entropy']
    features = [file_features.get('size', 0), file_features.get('entropy', 0.0)]
    prediction = model.predict([features])[0]
    return 'MALICIOUS' if prediction == 1 else 'SAFE'
