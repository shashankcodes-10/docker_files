# 🐳 Docker Projects

A collection of hands-on projects created while practicing **Docker, containerization, multi-stage builds, Docker Compose, networking, databases, reverse proxies, and multi-tier application architectures**.

Each project focuses on a different application stack and Docker use case.
Use the table below to quickly identify the **language, framework, database, tools, and architecture** used in each project.

## 📚 Projects

| #  | Project                                          | Application Stack            | Database   | Docker / Tools                                                    | Architecture         |
| -- | ------------------------------------------------ | ---------------------------- | ---------- | ----------------------------------------------------------------- | -------------------- |
| 1  | [Java Quotes App](./1.java-quotes-app)           | Java                         | —          | Docker, Multi-stage Build, Distroless                             | Single Tier          |
| 2  | [Flask App ECS](./2.flask-app-ecs)               | Python, Flask, Gunicorn      | —          | Docker, Multi-stage Build, Distroless, AWS ECR, ECS, ALB          | Single Tier Web App  |
| 3  | [DevOps Utilities API](./3.devops-utilities-api) | Python, FastAPI, Uvicorn     | —          | Docker, Multi-stage Build, Distroless, Boto3                      | Single Tier API      |
| 4  | [DevBoard UI](./4.devboard-ui)                   | React, Vite, JavaScript      | —          | Docker, Node.js, Multi-stage Build                                | Frontend Only        |
| 5  | [Two-Tier Flask App](./5.two-tier-flask-app)     | Python, Flask                | MySQL      | Docker, Docker Compose, Healthchecks, Volumes                     | **2-Tier**           |
| 6  | [Django Notes App](./6.django-notes-app)         | React + Django, Python       | MySQL      | Docker Compose, Nginx, Gunicorn, Multi-stage Builds, Volumes      | **3-Tier**           |
| 7  | [DevBoard](./7.devboard)                         | React + Go                   | PostgreSQL | Docker Compose, Nginx, Docker Hardened Images, Multi-stage Builds | **3-Tier**           |
| 8  | [SkillPulse](./8.SkillPulse)                     | HTML/CSS/JavaScript + Go/Gin | MySQL      | Docker Compose, Nginx, Docker Hardened Images                     | **3-Tier**           |
| 9  | [Chattingo](./9.chattingo)                       | React + Spring Boot, Java    | MySQL      | Docker Compose, Nginx, Maven, WebSocket, Multi-stage Builds       | **3-Tier**           |
| 10 | [AI BankApp](./10.AI-BankApp-DevOps)             | Java, Spring Boot, Thymeleaf | MySQL      | Docker Compose, Ollama, TinyLlama                                 | **3-Tier + AI Tier** |

## 🏗️ Architecture Progression

```text
Single Container
      │
      ▼
Frontend / API Containers
      │
      ▼
2-Tier
Application + Database
      │
      ▼
3-Tier
Frontend + Backend + Database
      │
      ▼
3-Tier + Additional Services
Application + Database + AI
```

## 🎯 Docker Concepts Covered

* Dockerfiles
* Docker images and containers
* Multi-stage builds
* Distroless images
* Docker Hardened Images
* Docker Compose
* Container networking
* Service-to-service communication
* Environment variables
* Healthchecks
* Persistent volumes
* Database containers
* Nginx reverse proxy
* Image size optimization
* Multi-tier containerized applications
* AWS ECS container deployment

> Each project directory contains its own README with detailed architecture, Docker configuration, implementation notes, and instructions for running the application.


## 👤 Original Authors
This project was originally created by **LondheShubham153**.

Original Repository: [https://github.com/LondheShubham153](https://github.com/LondheShubham153)
