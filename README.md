# MLOps Iris Pipeline (End-to-End ML Productionization)

This project demonstrates an end-to-end **MLOps + DevOps pipeline** using:

- Python (FastAPI + scikit-learn)
- MLflow (experiment tracking + artifact logging)
- Docker (containerization)
- GitHub Actions (CI/CD pipeline)
- Kubernetes (deployment + autoscaling)
- Terraform (infrastructure-as-code)
- Prometheus (metrics / monitoring)

---

## ✨ Features (what this repo showcases)

| Skill Area  | Demonstration |
|-------------|---------------|
| **MLOps**   | Model training + packaging + tracking (MLflow) |
| **DevOps**  | CI/CD pipeline with tests & Docker image build |
| **Cloud**   | Deployable to Kubernetes with autoscaling |
| **Monitoring** | Prometheus metrics exposed from FastAPI |

---

## 🏗 Architecture

**Training → Model artifact → Docker image → Deployment → Monitoring**

---

## 🚀 Run locally (quickstart)

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r src/requirements.txt

# Train model (saves trained model to /models/model.pkl)
python src/train.py

# Run API server
uvicorn src.app:app --reload --port 8000

# Terraform backoff config