"""Train a Random Forest classifier on the provided dataset."""
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib


def load_dataset(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}")
    return pd.read_csv(path)


def train_and_save(dataset_path: str, model_path: str):
    df = load_dataset(dataset_path)
    # features: we use file_size and entropy for simplicity
    X = df[['file_size', 'entropy']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)
    print("Classification report (test set):")
    print(classification_report(y_test, predictions))

    joblib.dump(clf, model_path)
    print(f"Model saved to {model_path}")


def main():
    dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'malware_dataset.csv')
    model_path = os.path.join(os.path.dirname(__file__), 'random_forest_model.joblib')
    train_and_save(dataset_path, model_path)


if __name__ == '__main__':
    main()
