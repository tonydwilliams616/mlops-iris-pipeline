import argparse
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import joblib
import os


def train(output_path: str = "models/model.pkl"):

    # Load dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Start MLflow experiment
    with mlflow.start_run():

        model = RandomForestClassifier(n_estimators=50, random_state=42)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # Log params & metrics to MLflow
        mlflow.log_param("n_estimators", 50)
        mlflow.log_metric("accuracy", acc)

        # Save model artifact
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        joblib.dump(model, output_path)
        mlflow.log_artifact(output_path, artifact_path="model")

        print(f"✅ Training complete — accuracy: {acc:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="models/model.pkl")
    args = parser.parse_args()

    train(output_path=args.output)
