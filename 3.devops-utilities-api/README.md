# Internal DevOps Utilities API

## 👨‍💻 My Docker Observations

I containerized this **FastAPI-based DevOps Utilities API** as part of my hands-on Docker and DevOps learning.

I experimented with both a **single-stage Docker build** and a **multi-stage Docker build** to compare their impact on the final image size.

---

## 🖥️ Application Output

The FastAPI application provides an interactive **Swagger UI** for the available API endpoints.

![FastAPI Application Output](./fastapi-output.png)

---

## 🐳 Docker Images

I built and uploaded both Docker images to Docker Hub.

### 🔗 Docker Hub

**[View Docker Images on Docker Hub](https://hub.docker.com/repository/docker/shashank971/fastapi-app/general)**

### Image Size Comparison

| Docker Build | Base Image / Approach                   | Observed Size |
| ------------ | --------------------------------------- | ------------: |
| Single-stage | `python:3.14-slim`                      |   **~270 MB** |
| Multi-stage  | `python:3.14-slim` → `python:3.14-slim` |   **~256 MB** |

### 📊 Result

The multi-stage build reduced the image size from approximately **270 MB to 256 MB**.

That's a reduction of approximately:

> **📉 14 MB (~5.2%)**

Although the reduction was relatively small, this was a useful Docker learning experiment.

### Why wasn't the reduction significant?

Multi-stage builds don't automatically make every application dramatically smaller.

In this project:

* The builder stage uses `python:3.14-slim`.
* The final stage also uses `python:3.14-slim`.
* The final image still requires the Python runtime and underlying system libraries.
* The application has relatively lightweight dependencies.
* There isn't a large compiled build artifact that can be removed from the final image.

Therefore, most of the image size still comes from the Python runtime, base OS libraries, and application dependencies.

> **Key takeaway:** Multi-stage builds provide the greatest size reduction when the build stage contains large build tools, compilers, caches, or development dependencies that are not required at runtime.

---

## 📦 Docker Hub Images

### Single-stage

```bash
docker pull shashank971/fastapi-app:latest
```

Run:

```bash
docker run -p 8000:8000 shashank971/fastapi-app:latest
```

### Multi-stage

If the multi-stage image has been pushed with a separate tag, pull that tag from the same Docker Hub repository.

```bash
docker pull shashank971/fastapi-app:<multistage-tag>
```

Then:

```bash
docker run -p 8000:8000 shashank971/fastapi-app:<multistage-tag>
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

## 🛠️ Tech Stack

| Component         | Technology           |
| ----------------- | -------------------- |
| Language          | Python 3.14          |
| Framework         | FastAPI              |
| ASGI Server       | Uvicorn              |
| System Metrics    | psutil               |
| AWS Integration   | Boto3                |
| API Documentation | Swagger UI / OpenAPI |
| Containerization  | Docker               |
| Base Image        | `python:3.14-slim`   |

---

## ✨ Features

* FastAPI-based REST API
* Interactive Swagger documentation
* Health check endpoint
* System metrics collection
* AWS resource utilities
* Log analysis utilities
* Modular router structure
* Dockerized application
* Single-stage and multi-stage Docker builds

---

## 📁 Project Structure

```text
devops-utilities-api/
├── app/
│   └── api.py                 # FastAPI application and route registration
│
├── routers/
│   ├── aws.py                # AWS-related API routes
│   ├── logs.py               # Log analysis API routes
│   └── metrics.py            # System metrics API routes
│
├── services/
│   ├── aws_service.py        # AWS service logic
│   ├── logs_service.py       # Log analysis logic
│   └── metrics_service.py    # System metrics logic
│
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
├── Dockerfile                # Single-stage Docker build
├── Dockerfile.multistage     # Multi-stage Docker build
├── fastapi-output.png        # Application screenshot
├── app.log                   # Application log file
└── README.md
```

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone <repo-url>
cd devops-utilities-api
```

### 2. Create a Python virtual environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## 🔌 API Endpoints

| Endpoint    | Method  | Purpose                  |
| ----------- | ------- | ------------------------ |
| `/`         | GET     | Basic API response       |
| `/health`   | GET     | Application health check |
| `/metrics`  | GET     | System metrics           |
| `/aws/...`  | Various | AWS-related operations   |
| `/logs/...` | Various | Log analysis operations  |

The complete list of available endpoints can be explored through the Swagger UI:

```text
http://localhost:8000/docs
```

---

## 🐳 Docker

### Single-Stage Build

Build the image:

```bash
docker build -t fastapi-app .
```

Run:

```bash
docker run -p 8000:8000 fastapi-app
```

### Multi-Stage Build

Build the multi-stage image:

```bash
docker build -f Dockerfile.multistage -t fastapi-app:multistage .
```

Run:

```bash
docker run -p 8000:8000 fastapi-app:multistage
```

---

## 📌 Docker Learning Takeaway

This project helped me understand that **multi-stage builds are not solely about reducing image size**.

They are useful for separating the:

```text
Build Environment
       ↓
Dependencies / Build
       ↓
Production Runtime
```

However, the final runtime image still determines how much space is actually saved.

In this experiment:

```text
Single-stage     ~270 MB
       ↓
Multi-stage      ~256 MB
```

So the reduction was only around **14 MB**.

The next optimization step would be to investigate the Python runtime/base image and dependency footprint rather than relying only on a multi-stage build.

This experiment gave me a better practical understanding of **Docker layers, base images, dependencies, and multi-stage builds**.

---

##  Original Project / Author

This project was originally taken from **Shubham Londhe**.

**Author / source repository:**

https://github.com/LondheShubham153

The Dockerization, Docker image-size comparison, multi-stage Docker experimentation, and observations documented in this README are my own hands-on work.
