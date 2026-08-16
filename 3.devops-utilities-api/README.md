# Internal DevOps Utilities API

## 👨‍💻 My Docker Observations

I containerized this **FastAPI-based DevOps Utilities API** as part of my hands-on Docker and DevOps learning.

I experimented with **three different Docker approaches** to understand how base images, multi-stage builds, and Distroless images affect container size and production runtime.

### Docker approaches tested

1. **Single-stage Docker build**
2. **Multi-stage Docker build**
3. **Multi-stage build with a Distroless runtime**

This experiment helped me understand that **multi-stage builds do not automatically result in a dramatically smaller image**. The amount of reduction depends heavily on the application, dependencies, build tools, and runtime image.

---

## 🖥️ Application Output

The FastAPI application provides an interactive **Swagger UI** for the available API endpoints.

![FastAPI Application Output](./fastapi-output.png)

---

# 🐳 Docker Image Comparison

I built and uploaded the Docker images to Docker Hub.

### 🔗 Docker Hub

**[View Docker Images on Docker Hub](https://hub.docker.com/repository/docker/shashank971/fastapi-app/general)**

### Image Size Comparison

| Docker Build | Base Image / Approach                            | Observed Size |
| ------------ | ------------------------------------------------ | ------------: |
| Single-stage | `python:3.14-slim`                               |   **~270 MB** |
| Multi-stage  | `python:3.14-slim → python:3.14-slim`            |   **~256 MB** |
| Distroless   | `python:3.13-slim → distroless/python3-debian13` |   **~167 MB** |

### 📊 Results

The three experiments produced:

```text
Single-stage
~270 MB
     ↓
Multi-stage
~256 MB
     ↓
Distroless
~167 MB
```

Compared with the single-stage image, the Distroless image reduced the size by approximately:

> **📉 103 MB (~38%)**

Compared with the regular multi-stage image:

> **📉 89 MB (~35%)**

The results demonstrated that **changing the production runtime image can have a much larger impact than simply adding another Docker build stage**.

---

# 🔍 Why Was the Multi-stage Reduction Small?

The regular multi-stage Dockerfile uses:

```text
python:3.14-slim
        ↓
python:3.14-slim
```

Both the builder and production stages use essentially the same Python runtime and underlying base image.

The production image still needs:

* Python runtime
* Python dependencies
* System libraries
* Application source code

Therefore, the multi-stage build only removed a relatively small amount of unnecessary build-layer content.

This resulted in:

```text
Single-stage     ~270 MB
Multi-stage      ~256 MB
```

A reduction of approximately:

> **14 MB (~5.2%)**

---

# 🧊 Distroless Experiment

I also created a **multi-stage Docker build using a Distroless Python runtime**.

The architecture is:

```text
Python 3.13-slim
       ↓
Install dependencies
       ↓
Build stage
       ↓
Distroless Python 3.13
       ↓
FastAPI + Uvicorn
```

The resulting image size was:

> **~167 MB**

### Why Python 3.13?

The selected Distroless runtime was:

```text
gcr.io/distroless/python3-debian13
```

This runtime uses **Python 3.13**.

Initially, the project was using Python 3.14:

```text
Python 3.14 builder
        ↓
Python 3.13 Distroless runtime
```

This caused a runtime compatibility problem with `pydantic-core`.

The application produced:

```text
ModuleNotFoundError:
No module named 'pydantic_core._pydantic_core'
```

The issue occurred because `pydantic-core` contains native/compiled components that were installed for Python 3.14 but were being executed using Python 3.13.

Therefore, for the Distroless experiment, I changed the builder to Python 3.13:

```text
Python 3.13-slim
        ↓
Python 3.13 Distroless
```

This kept the Python runtime and compiled dependencies compatible.

### Why Distroless?

Distroless images contain only the components required to run the application and intentionally omit many unnecessary operating-system utilities.

They generally do not include:

* Shell
* Package manager
* Compilers
* Unnecessary command-line utilities
* Development tooling

This provides a more minimal production runtime and can reduce the attack surface.

In this experiment, moving from:

```text
python:3.14-slim
```

to:

```text
gcr.io/distroless/python3-debian13
```

resulted in a significant reduction:

```text
~256 MB
     ↓
~167 MB
```

That's approximately:

> **📉 89 MB (~35%) reduction**

---

# 📦 Docker Hub Images

### Single-stage

Pull:

```bash
docker pull shashank971/fastapi-app:latest
```

Run:

```bash
docker run -p 8000:8000 shashank971/fastapi-app:latest
```

### Multi-stage

Pull the multi-stage tag:

```bash
docker pull shashank971/fastapi-app:<multistage-tag>
```

Run:

```bash
docker run -p 8000:8000 shashank971/fastapi-app:<multistage-tag>
```

### Distroless

Pull the Distroless tag:

```bash
docker pull shashank971/fastapi-app:<distroless-tag>
```

Run:

```bash
docker run -p 8000:8000 shashank971/fastapi-app:<distroless-tag>
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

---

# 🛠️ Tech Stack

| Component               | Technology                           |
| ----------------------- | ------------------------------------ |
| Language                | Python 3.14                          |
| Framework               | FastAPI                              |
| ASGI Server             | Uvicorn                              |
| System Metrics          | psutil                               |
| AWS Integration         | Boto3                                |
| API Documentation       | Swagger UI / OpenAPI                 |
| Containerization        | Docker                               |
| Single-stage Base Image | `python:3.14-slim`                   |
| Multi-stage Runtime     | `python:3.14-slim`                   |
| Distroless Builder      | `python:3.13-slim`                   |
| Distroless Runtime      | `gcr.io/distroless/python3-debian13` |

> **Note:** Python 3.13 is used specifically for the Distroless experiment to match the selected Distroless Python runtime.

---

# ✨ Features

* FastAPI-based REST API
* Interactive Swagger documentation
* Health check endpoint
* System metrics collection
* AWS resource utilities
* Log analysis utilities
* Modular router structure
* Dockerized application
* Single-stage Docker build
* Multi-stage Docker build
* Distroless runtime experimentation
* Docker image-size comparison
* Python runtime compatibility testing

---

# 📁 Project Structure

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
├── Dockerfile.distroless     # Multi-stage + Distroless Docker build
├── fastapi-output.png        # Application screenshot
├── app.log                   # Application log file
└── README.md
```

---

# 🚀 Running Locally

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

# 🔌 API Endpoints

| Endpoint    | Method  | Purpose                  |
| ----------- | ------- | ------------------------ |
| `/`         | GET     | Basic API response       |
| `/health`   | GET     | Application health check |
| `/metrics`  | GET     | System metrics           |
| `/aws/...`  | Various | AWS-related operations   |
| `/logs/...` | Various | Log analysis operations  |

The complete list of available endpoints can be explored through Swagger UI:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker

## Single-Stage Build

Build:

```bash
docker build -t fastapi-app .
```

Run:

```bash
docker run -p 8000:8000 fastapi-app
```

---

## Multi-Stage Build

Build:

```bash
docker build -f Dockerfile.multistage -t fastapi-app:multistage .
```

Run:

```bash
docker run -p 8000:8000 fastapi-app:multistage
```

---

## Distroless Build

Build:

```bash
docker build -f Dockerfile.distroless -t fastapi-app:distroless .
```

Run:

```bash
docker run -p 8000:8000 fastapi-app:distroless
```

The Distroless image uses Python 3.13 to match the selected Distroless runtime.

---

# 📌 Docker Learning Takeaway

This project helped me understand that **multi-stage builds are not solely about reducing image size**.

The key concept is separating:

```text
Build Environment
       ↓
Install / Build
       ↓
Production Runtime
```

The final image should contain only what is required to run the application.

### What I learned

```text
Single-stage
Python 3.14-slim
       ↓
~270 MB


Multi-stage
Python 3.14-slim
       ↓
Python 3.14-slim
       ↓
~256 MB


Distroless
Python 3.13-slim
       ↓
Distroless Python 3.13
       ↓
~167 MB
```

### Key observations

**1. Multi-stage builds don't automatically guarantee huge size reductions.**

The reduction depends on how different the build environment is from the production runtime.

**2. Runtime image selection matters.**

Changing from a full Python runtime image to a Distroless runtime produced a much larger reduction in this experiment.

**3. Python dependencies matter.**

Packages such as `pydantic-core` may contain native components, so the Python version used to build dependencies must be compatible with the Python runtime.

**4. Smaller doesn't always mean better.**

A production image should balance:

```text
Size
+
Security
+
Compatibility
+
Maintainability
+
Reliability
```

### Final comparison

```text
                  Image Size

Single-stage       ████████████████████████████  ~270 MB
Multi-stage        ██████████████████████████    ~256 MB
Distroless         █████████████████             ~167 MB
```

> **Final takeaway:** This experiment gave me practical experience with Docker image optimization, base image selection, multi-stage builds, Distroless runtimes, Python dependency compatibility, and the trade-offs involved in designing production container images.

---

# Original Project / Author

This project was originally taken from **Shubham Londhe**.

**Author / source repository:**

https://github.com/LondheShubham153

The Dockerization, Docker image-size comparison, multi-stage Docker experimentation, Distroless experimentation, Python runtime compatibility testing, and observations documented in this README are my own hands-on work.
