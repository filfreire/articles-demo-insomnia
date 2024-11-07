# articles-demo-insomnia

Example Demo for tinkering with Insomnia API Client

## Setup

- Install Python (e.g. version 3.11)
- Run `make install dev`.

### Docker setup

- Install Docker
- Run `make docker-build docker-run`.

## Running in Docker

Run on terminal:

```bash
docker run -d --name articles-app -p 3000:3000 ghcr.io/filfreire/articles-demo-insomnia:latest
```
