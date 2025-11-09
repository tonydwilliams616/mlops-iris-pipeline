import os
import sys
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Ensure model exists before app import
os.makedirs("models", exist_ok=True)
iris = load_iris()
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(iris.data, iris.target)
joblib.dump(clf, "models/model.pkl")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def setup_module(module):
    """Create a small model file before tests run."""
    iris = load_iris()
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(iris.data, iris.target)
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/model.pkl")


def test_health():
    """Check the health endpoint returns OK."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict():
    iris = load_iris()
    sample = iris.data[:2].tolist()
    response = client.post("/predict", json={"instances": sample})
    print("DEBUG RESPONSE:", response.json())
    assert response.status_code == 200
    assert "predictions" in response.json()