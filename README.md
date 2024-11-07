# articles-insomnia

Example Demo for tinkering with Insomnia API Client

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Groceries%20API&uri=https%3A%2F%2Fraw.githubusercontent.com%2Ffilfreire%2Fgroceries-insomnia%2Fmain%2Finsomnia-workspace.yaml)

## Setup

- Install Python (e.g. version 3.11)
- Run `make install dev`.

### Docker setup

- Install Docker
- Run `make docker-build docker-run`.

## Running in Docker

Run on terminal:

```bash
docker run -d --name articles-app -p 3000:3000 ghcr.io/filfreire/articles-insomnia:latest
```

## Side-notes

- Code used on <https://www.youtube.com/watch?v=30vI6Oq865s>
- Code used on [API Summit 2024 Insomnia presentation](https://konghq.com/events/conferences/api-summit/agenda)
