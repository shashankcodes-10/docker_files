# Flask App — AWS ECS Deployment

## 🖥️ Application Output

The Flask application was successfully built and run using Docker.

![Flask App Output](./flask-app-output.png)

The screenshot above shows the running Flask application with:

- **Flask 3.1.1**
- **Python 3.14**
- **AWS ECS** as the target deployment platform
- **Gunicorn** serving as the production-ready WSGI web server

---

# 🔗 Docker Hub

The Docker image is available on Docker Hub:

**Docker Hub Repository:**

https://hub.docker.com/repository/docker/shashank971/flask-app-ecs/general

## Pull the Image

```bash
docker pull shashank971/flask-app-ecs:latest
```

## Run the Image

```bash
docker run -p 80:80 shashank971/flask-app-ecs:latest
```

# 👨‍💻 My Observations & Contributions

I used this project as part of my hands-on learning with **Docker, Python, Flask, and AWS ECS**.

During the process, I experimented with Docker image optimization and introduced **Gunicorn** as a production-ready WSGI server.

## ⚡ Production-Grade Gunicorn WSGI Server

The original setup relied on Flask's built-in development server, which is intended for development and local testing rather than production workloads.

### What I Did

- Added `gunicorn` to `requirements.txt`.
- Configured the Docker container to run the Flask application using Gunicorn.
- Kept Flask's development server available for local development and debugging.

### Why It Matters

Gunicorn is a production-oriented WSGI server that can use multiple worker processes to handle requests concurrently.

This makes it more suitable for deploying Flask applications behind services such as:

- AWS ECS
- AWS Application Load Balancer
- Docker
- Cloud-based production environments

---

# 🐳 Docker Image Size Comparison

I tested both the single-stage and multi-stage Docker builds.

| Docker Build | Approach | Observed Image Size |
|---|---|---:|
| Single-stage | `python:3.14-slim` | **~200 MB** |
| Multi-stage | `python:3.14-slim` → Distroless | **~105 MB** |

## 📊 Result

The multi-stage Docker build reduced the image size from approximately **200 MB to 105 MB**.

That's a reduction of approximately:

> **📉 ~95 MB (~47.5% smaller)**

This experiment helped me understand how separating the **build environment** from the **runtime environment** can significantly reduce the final Docker image size.

## Why Did the Multi-Stage Image Become Smaller?

The multi-stage Dockerfile uses:

1. **Builder stage** — `python:3.14-slim` is used to install the required dependencies.
2. **Runtime stage** — only the required application files and dependencies are copied into a lightweight **distroless** image.

The final image does not need unnecessary build-time components such as:

- `pip`
- Shell utilities
- Package installation tools
- Other unnecessary OS utilities

This results in:

- Smaller final image
- Reduced attack surface
- Fewer unnecessary components
- Better separation between build and runtime environments

> **Note:** The image sizes are based on my local builds. Actual image sizes can vary depending on the exact base image version, CPU architecture, dependency versions, Docker version, and build configuration.

---

# 📊 Docker Image Optimization

## Before — Single Stage

```text
python:3.14-slim
       ↓
Application + Dependencies
       ↓
~200 MB
```

## After — Multi Stage + Distroless

```text
             Builder Stage
                  ↓
          python:3.14-slim
                  ↓
        Install dependencies
                  ↓
             Application
                  ↓
            Runtime Stage
                  ↓
              Distroless
                  ↓
              ~105 MB
```

## Image Size Result

```text
Single-stage     ~200 MB
       ↓
Multi-stage      ~105 MB
       ↓
Reduction        ~95 MB
```

The multi-stage build resulted in approximately **47.5% reduction** in image size.

### 💡 Key Docker Takeaway

> **Build with everything you need, but run with only what you need.**

The builder image does not need to be carried into production.

Multi-stage builds allow build-time dependencies to remain in the builder stage while keeping the final runtime image focused only on the application and its required runtime dependencies.

---



---

# 📌 Project Overview

A minimal Flask web application built for learning containerization and deployment to **AWS ECS (Elastic Container Service)**.

This project provides a simple Flask-based web interface with a health-check endpoint designed for use with an AWS Application Load Balancer.

---

# ✨ Features

- Responsive landing page
- Modern glassmorphism UI
- Flask REST endpoint
- `/health` endpoint for ECS load balancer health checks
- Production-ready Gunicorn WSGI server
- Dockerized application
- Single-stage Docker build
- Multi-stage Docker build
- Distroless runtime image
- AWS ECS deployment support
- AWS Application Load Balancer health checks

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Framework | Flask 3.1.1 |
| Web Server | Gunicorn |
| Runtime | Python 3.14 |
| Containerization | Docker |
| Development Base Image | `python:3.14-slim` |
| Production Runtime | Distroless |
| Deployment | AWS ECS |
| Load Balancer | AWS Application Load Balancer |
| Port | 80 |

---

# 📁 Project Structure

```text
flask-app-ecs/
│
├── app.py
│   └── Flask application and routes
│
├── run.py
│   └── Local development entry point
│
├── requirements.txt
│   └── Python dependencies including Gunicorn
│
├── templates/
│   └── index.html
│       └── Flask landing page
│
├── Dockerfile
│   └── Single-stage Docker build
│
├── Dockerfile-multi
│   └── Multi-stage Docker build with distroless runtime
│
├── flask-app-output.png
│   └── Application output screenshot
│
└── README.md
    └── Project documentation
```

---

# ⚙️ Quick Start

## 1. Clone the Repository

```bash
git clone <repo-url>
cd flask-app-ecs
```

## 2. Create a Python Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
python run.py
```

The application runs locally at:

```text
http://localhost:80
```

---

# 🐳 Run with Docker

## Single-Stage Build

Build the image:

```bash
docker build -t flask-app .
```

Run the container:

```bash
docker run -p 80:80 flask-app
```

Open:

```text
http://localhost
```

---

## Multi-Stage Build

Build the multi-stage image:

```bash
docker build -f Dockerfile-multi -t flask-app:multistage .
```

Run the container:

```bash
docker run -p 80:80 flask-app:multistage
```

Open:

```text
http://localhost
```

---

# 🐳 Dockerfiles Explained

## Simple — `Dockerfile`

The single-stage Dockerfile uses:

```text
python:3.14-slim
```

It:

1. Creates the application working directory.
2. Copies the project files.
3. Installs Python dependencies.
4. Exposes port `80`.
5. Runs the Flask application using Gunicorn.

### Observed Image Size

> **~200 MB**

This approach is simple and useful for learning and development.

---

## Multi-Stage — `Dockerfile-multi`

The multi-stage Dockerfile separates the build and runtime environments.

### Stage 1 — Builder

The builder stage uses:

```text
python:3.14-slim
```

The required Python dependencies are installed in the builder environment.

### Stage 2 — Runtime

The final stage uses a **distroless runtime image**.

Only the required application files and dependencies are copied into the final image.

### Observed Image Size

> **~105 MB**

### Benefits

- Smaller final image
- Reduced attack surface
- No `pip` in the final runtime image
- No shell in the final runtime image
- No unnecessary OS utilities
- Separation of build-time and runtime dependencies
- Better suited for production deployment

---

# ⚡ Gunicorn Configuration

For production, Gunicorn can load the Flask application directly.

Using `app.py`:

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
```

Alternatively, if `run.py` exposes the Flask application:

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:80", "run:app"]
```

Gunicorn acts as the production WSGI server between the Flask application and incoming HTTP requests.

```text
Client
   ↓
AWS Application Load Balancer
   ↓
Gunicorn
   ↓
Flask Application
   ↓
Response
```

---

# 🔌 Endpoints

| Route | Method | Description |
|---|---|---|
| `/` | GET | Landing page |
| `/health` | GET | Health check |

The `/health` endpoint returns:

```text
Server is up and running
```

The `/health` endpoint can be configured as the health-check path for the AWS Application Load Balancer.

---

# ☁️ Deploy to AWS ECS

High-level steps to deploy this application on AWS ECS.

## 1. Push Image to Amazon ECR

Login to ECR:

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

Tag the image:

```bash
docker tag flask-app:latest <account-id>.dkr.ecr.<region>.amazonaws.com/flask-app:latest
```

Push the image:

```bash
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/flask-app:latest
```

## 2. Create ECS Task Definition

Specify:

- ECR image
- Container port `80`
- CPU
- Memory
- Container health check if required

## 3. Create ECS Service

Configure:

- ECS Cluster
- Desired task count
- Networking
- Security groups
- Application Load Balancer

## 4. Configure Application Load Balancer

Create a target group pointing to:

```text
Port: 80
```

Configure the health check path:

```text
/health
```

---

# 🔄 Deployment Architecture

The overall deployment flow is:

```text
Developer
    ↓
Docker Build
    ↓
Docker Image
    ↓
Amazon ECR
    ↓
ECS Task
    ↓
ECS Service
    ↓
Application Load Balancer
    ↓
Gunicorn
    ↓
Flask Application
```

---

# 📚 Docker Learning Takeaway

This project demonstrated the significant impact that **multi-stage Docker builds** can have on image size.

### Image Size Before

**Single-stage: ~200 MB**

### Image Size After

**Multi-stage + Distroless: ~105 MB**

### Total Reduction

**~95 MB / ~47.5% smaller**

The main lesson from this experiment was:

> **Build with everything you need, but run with only what you need.**

Using a separate builder stage allows build-time dependencies to stay out of the final production image.

The use of a distroless runtime further removes unnecessary utilities and reduces the final container footprint.

This experiment gave me practical experience with:

- Docker image optimization
- Multi-stage builds
- Distroless images
- Python containerization
- Gunicorn
- Docker networking
- AWS ECS deployment concepts
- Application Load Balancer health checks

---

# 🙏 Original Project / Author

This project was originally taken from **Shubham Londhe / TrainWithShubham**.

### Author / Source Repository

https://github.com/LondheShubham153

The Dockerization, Gunicorn integration, multi-stage Docker build, image-size comparison, and observations documented above are my own hands-on work.
