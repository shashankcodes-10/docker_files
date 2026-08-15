# Flask App — AWS ECS Deployment

### 🖥️ Application Output

The Flask application was successfully built and run using Docker.

![Flask App Output](./flask-app-output.png)

The screenshot above shows the running Flask application with:

* **Flask 3.1.1**
* **Python 3.14**
* **AWS ECS** as the target deployment platform
* **Gunicorn** serving as the production-ready WSGI web server

## 👨‍💻 My Observations & Contributions

I used this project as part of my hands-on learning with **Docker, Python, Flask, and AWS ECS**. To elevate this project to real-world production standards, I introduced performance and architectural improvements.

### ⚡ Feature Contribution: Production-Grade Gunicorn WSGI Server
The original setup relied on Flask's built-in development server, which is single-threaded and not designed for production traffic. 
* **What I Did:** I added `gunicorn` to the `requirements.txt` dependencies.
* **Why It Matters:** Gunicorn enables the application to handle multiple requests concurrently via multiple worker processes. This prevents the server from freezing under load, makes it highly resilient, and drastically increases request processing speeds on AWS ECS.

### 🐳 Docker Image

I built the application using the `python:3.14-slim` base image.

The resulting Docker image size was approximately:

> **📦 Image Size: ~200 MB**

This helped me understand how the choice of base image and installed dependencies affects the final Docker image size.

### 🔗 Docker Hub

The Docker image is available on Docker Hub:

**[https://hub.docker.com/repository/docker/shashank971/flask-app-ecs/general](https://hub.docker.com/repository/docker/shashank971/flask-app-ecs/general)**

You can pull the image using:

```bash
docker pull shashank971/flask-app-ecs:latest
```

And run it with:

```bash
docker run -p 80:80 shashank971/flask-app-ecs:latest
```

### 📊 Docker Image Size Observation

| Base Image         | Observed Image Size |
| ------------------ | ------------------: |
| `python:3.14-slim` |         **~200 MB** |

> **Note:** The image size is based on my local build. Actual image size can vary depending on the exact base image version, architecture, installed dependencies, and Docker configuration.

The project also includes a **multi-stage Dockerfile using a distroless runtime image**, which can be explored to further reduce the final image size and attack surface.

---

# Original Project Documentation

A minimal Flask web application built for learning containerization and deployment to **AWS ECS (Elastic Container Service)**.

Part of the [TrainWithShubham](https://github.com/TrainWithShubham) — DevOps Zero To Hero course.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.1-green)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)
![AWS ECS](https://img.shields.io/badge/AWS-ECS-FF9900)

## Features

* Responsive landing page with modern glassmorphism UI
* `/health` endpoint for ECS load balancer health checks
* Production-ready **Gunicorn WSGI web server** capability
* Two Dockerfiles — simple and multistage (distroless)

## Tech Stack

| Component | Technology                        |
| --------- | --------------------------------- |
| Framework | Flask 3.1.1                       |
| Web Server| Gunicorn (Production-ready)       |
| Runtime   | Python 3.14                       |
| Container | Docker (python-slim / distroless) |
| Deploy    | AWS ECS                           |

## Project Structure

```text
flask-app-ecs/
├── app.py                 # Flask app containing defined routes
├── run.py                 # Local testing script / Alternative Entry point
├── requirements.txt       # Python dependencies (includes Gunicorn)
├── templates/
│   └── index.html         # Landing page
├── Dockerfile             # Simple single-stage build using Gunicorn
└── Dockerfile-multi       # Multistage build with distroless
```

## Quick Start & Entry Points

This project is highly flexible. Depending on your environment, you can run the server directly using **`app.py`** or use **`run.py`** to boot your application.

### 1. Run locally (Development mode)
For immediate local changes and debugging, install your dependencies and use `run.py` to trigger Flask's built-in hot reloading:

```bash
pip install -r requirements.txt
python run.py
```
App runs locally at **http://localhost:80**.

### 2. Run with Docker (Production Gunicorn Mode)
When containerizing the application, you can execute the production server targeting either entry point. Gunicorn bypasses local files entirely and loads the Flask instance into memory.

**Using `app.py` directly (Standard Approach):**
```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
```

**Using `run.py` (Alternative Entrypoint if handling pre-imports):**
```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:80", "run:app"]
```

#### Build and Launch commands:

**Simple build:**
```bash
docker build -t flask-app .
docker run -p 80:80 flask-app
```

**Multistage build (smaller, production-grade):**
```bash
docker build -f Dockerfile-multi -t flask-app .
docker run -p 80:80 flask-app
```

## Dockerfiles Explained

### Simple (`Dockerfile`)

Single-stage build using `python:3.14-slim`. Copies everything, installs dependencies (including Gunicorn), and maps execution cleanly through the optimized `exec` array command.

### Multistage (`Dockerfile-multi`)

Two-stage build:

1. **Builder stage** — installs dependencies into a separate directory using `python:3.14-slim`
2. **Final stage** — copies only the app and deps into a `distroless` image

Benefits:

* Smaller final image (no pip, no shell, no OS utilities)
* Reduced attack surface — distroless images contain only the app and its runtime
* Better layer caching — dependencies are copied before source code

## Endpoints

| Route     | Method | Description                                       |
| --------- | ------ | ------------------------------------------------- |
| `/`       | GET    | Landing page                                      |
| `/health` | GET    | Health check (returns `Server is up and running`) |

## Deploy to AWS ECS

High-level steps to deploy this app on ECS:

1. **Push image to ECR**

   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
   docker tag flask-app:latest <account-id>.dkr.ecr.<region>.amazonaws.com/flask-app:latest
   docker push <account-id>.dkr.ecr.<region>.amazonaws.com/flask-app:latest
   ```

2. **Create ECS Task Definition** — specify the ECR image, port 80, memory/CPU limits

3. **Create ECS Service** — attach to a cluster, configure desired count, link to a load balancer

4. **Configure ALB** — target group pointing to port 80, use `/health` as the health check path


