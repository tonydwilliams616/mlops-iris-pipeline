# --------------------------------------------------
# Stage 1 — Build and install dependencies
# --------------------------------------------------
FROM python:3.11-slim AS base

WORKDIR /app

# Copy requirements and install
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Create model directory (so model volume can mount here)
RUN mkdir -p /app/models

# Expose app port
EXPOSE 8000

# Default environment variable for model path
ENV MODEL_PATH=/app/models/model.pkl

# Entrypoint
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]