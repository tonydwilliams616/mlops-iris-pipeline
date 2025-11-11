train:
	python src/train.py

run:
	uvicorn src.app:app --reload --port 8000

docker-build:
	docker build -t mlops-iris:latest -f docker/Dockerfile .

docker-run:
	docker run -p 8000:8000 -v $(PWD)/models:/app/models mlops-iris:latest

test:
	pytest -v

deploy-k8s:
	kubectl apply -f k8s/