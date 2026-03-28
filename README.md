# Flask Calculator API 🐳

A simple REST API built with Flask, containerized with Docker, and deployed via GitHub Actions CI/CD pipeline.

## What it does
A calculator API that performs basic math operations via HTTP endpoints.

## Endpoints
| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /` | Health check | `localhost:5000/` |
| `GET /add` | Add two numbers | `localhost:5000/add?a=2&b=3` |
| `GET /subtract` | Subtract two numbers | `localhost:5000/subtract?a=10&b=4` |
| `GET /multiply` | Multiply two numbers | `localhost:5000/multiply?a=3&b=4` |

## Tech Stack
- **Python** — Flask REST API
- **pytest** — Automated testing
- **Docker** — Containerization
- **GitHub Actions** — CI/CD pipeline

## CI/CD Pipeline
On every push to `main`:
1. Runs pytest tests automatically
2. If tests pass — builds Docker image
3. Pushes image to Docker Hub

## Run locally with Docker
```bash
docker pull atiquehashmi2346/flask-calculator:latest
docker run -p 5000:5000 atiquehashmi2346/flask-calculator:latest
```

Then visit `http://localhost:5000`

## Run tests locally
```bash
pip install -r requirements.txt
pytest test_app.py
```