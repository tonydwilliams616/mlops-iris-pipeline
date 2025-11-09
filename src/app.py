from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import joblib
import numpy as np
import os

app = FastAPI(title="Iris MLOps Service")

# --------------------------------------------------
# Metrics for Prometheus
# --------------------------------------------------
REQUEST_COUNT = Counter("request_count", "Total request count", ["endpoint"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency", ["endpoint"])

# --------------------------------------------------
# Model loading
# --------------------------------------------------
MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception:
    model = None
    print(f"⚠️ Warning: could not load model from {MODEL_PATH}. Run training first.")


# --------------------------------------------------
# Request model
# --------------------------------------------------
class PredictRequest(BaseModel):
    instances: list


# --------------------------------------------------
# Routes
# --------------------------------------------------
@app.on_event("startup")
def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        print(f"⚠️ Model not found at {MODEL_PATH}, creating a dummy model for startup.")
        from sklearn.datasets import load_iris
        from sklearn.ensemble import RandomForestClassifier
        iris = load_iris()
        clf = RandomForestClassifier(n_estimators=10, random_state=42)
        clf.fit(iris.data, iris.target)
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(clf, MODEL_PATH)
    model = joblib.load(MODEL_PATH)

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest):
    REQUEST_COUNT.labels(endpoint="/predict").inc()
    with REQUEST_LATENCY.labels(endpoint="/predict").time():
        if model is None:
            raise HTTPException(status_code=500, detail="Model not loaded.")
        try:
            X = np.array(request.instances)
            preds = model.predict(X).tolist()
            return {"predictions": preds}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


@app.get("/metrics")
def metrics():
    """Expose Prometheus metrics endpoint."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)