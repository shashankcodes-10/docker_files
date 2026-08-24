# Django Notes App

A simple notes application built with React, Django REST Framework, and MySQL.

## Project Structure

```text
.
├── frontend/       # React application + Nginx
├── backend/        # Django REST API
├── docker-compose.yml
├── .env
└── Jenkinsfile
```

## Stack

- React 18
- Django 4.1.5
- Django REST Framework 3.14
- MySQL 8
- Nginx
- Gunicorn
- Docker Compose

## Run with Docker Compose

```bash
docker compose up --build
```

Open:

```text
http://localhost
```

The React frontend is served by Nginx. API requests under `/api/` and Django admin requests under `/admin/` are reverse-proxied to the backend container.

## Services

- `frontend` → Nginx + React production build → port 80
- `backend` → Django + Gunicorn → port 8000
- `db` → MySQL → port 3306 inside the Compose network

## Backend

The backend runs migrations when the container starts and collects Django static files during the image build.
