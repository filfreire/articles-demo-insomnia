# articles-demo-insomnia

Example Demo for tinkering with Insomnia API Client

## Setup

- Install Python (e.g. version 3.11)
- Run `make install dev`.

### CI Setup

Be sure to define the following repository secrets:

```plaintext
DEPLOY_PATH
PSWD
REMOTE_HOST
REMOTE_USER
SSH_KEY
TAILSCALE_AUTHKEY
```

### Docker setup

- Install Docker
- Run `make docker-build docker-run`.

## Running in Docker

Run on terminal:

```bash
docker run -d --name articles-app -p 3000:3000 ghcr.io/filfreire/articles-demo-insomnia:latest
```

## Usage Examples

### Add Article

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "article": {
        "author": "Jane Smith",
        "title": "Understanding OpenAPI",
        "publisher": "TechPress",
        "year": 2023
    }
}' http://localhost:3000/add_article
```

### Get Articles

```bash
curl http://localhost:3000/get_articles
```

### Delete Article

```bash
curl -X DELETE -H "Content-Type: application/json" -d '{
    "article": {
        "author": "Jane Smith",
        "title": "Understanding OpenAPI"
    }
}' http://localhost:3000/delete_article
```
