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

terraform init -backend-config=backend-dev.conf

---

## ☁️ Terraform Remote Backend (S3 + DynamoDB)

In production environments, Terraform state should never be stored locally.  
Instead, this project uses an **S3 backend** for state locking.

### 🏗 Why this matters
| Feature | Benefit |
|----------|----------|
| **S3 remote state** | Secure, versioned, team-accessible |
| **Environment configs** | Separate backends for `dev`, `staging`, `prod` |
| 

---

### ⚙️ Backend configuration

Terraform’s backend can’t use variables directly,  
so we use a clean, flexible approach with **per-environment backend config files**.

In `terraform/backend-dev.conf`:
```hcl
bucket         = "mlops-terraform-state-dev"
key            = "infra/terraform.tfstate"
region         = "us-east-1"
dynamodb_table = "mlops-terraform-locks-dev"
encrypt        = true