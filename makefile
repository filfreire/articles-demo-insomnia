install:
	python3 -m venv .venv
	python3 -m pip install --no-cache-dir -r requirements.txt

dev:
	python3 app.py

docker-build:
	docker build -t articles-app .

docker-run:
	docker run -d --name articles-app -p 3000:3000 articles-app

docker-run-image:
	docker run -d --name articles-app -p 3000:3000 ghcr.io/filfreire/articles-insomnia:latest