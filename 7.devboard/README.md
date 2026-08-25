# DevBoard — Advanced (React + Go + PostgreSQL)

DevBoard is a full-stack task and project management application built with a React frontend, Go backend, and PostgreSQL database.

The application uses real persistent database data instead of in-memory mock data.

![DevBoard Application](./devboard.png)

## My Changes & Application Output

| My Changes | Application Output |
|---|---|
| **Containerized the complete application stack** with React frontend, Go backend, and PostgreSQL database using Docker Compose. | ![DevBoard Application](./assets/devboard.png) |
| **Implemented multi-stage Docker builds** for the frontend and backend to separate build dependencies from runtime images. | The application is running successfully with real project and task data loaded from PostgreSQL. |
| **Used Docker Hardened Images (DHI)** for the Node.js and Go build/runtime stages where applicable. | Nginx serves the production React build and routes `/api/` requests to the Go backend. |
| **Added Nginx reverse-proxy routing** between the React frontend and Go API. | React frontend, Go API, and PostgreSQL communicate through the Docker network. |
| **Added PostgreSQL persistence and initialization** using Docker volumes and the `init/postgres/` SQL files. | Database-backed projects and tasks are displayed in the DevBoard UI. |
| **Added environment-based configuration** for backend and PostgreSQL settings. | The stack is accessible through the frontend entry point on the configured host port. |
| **Added container healthchecks** for PostgreSQL and backend readiness. | The application is shown in the screenshot above running as the completed full-stack version. |

## Architecture

Browser → Nginx → React frontend  
                     ↓  
                 Go backend → PostgreSQL

Nginx acts as the single entry point for the application. It serves the React production build and reverse-proxies `/api/` requests to the Go backend.

## Project Components

### Frontend

- React application built with Vite
- Production assets generated during a multi-stage Docker build
- Node.js is used only during the build stage
- Nginx serves the final static React files
- Nginx handles SPA routing so React routes continue to work after page refreshes
- `/api/` requests are forwarded to the Go backend

### Backend

- Go REST API
- Reads and writes project and task data in PostgreSQL
- Provides a health endpoint
- Runs as a compiled Go binary
- Uses a multi-stage Docker build so the final image contains the application binary rather than the source and build dependencies

### Database

- PostgreSQL
- Persistent Docker volume for database data
- Initialization scripts create the database schema and load example data on the first database initialization
- Database readiness is checked with a PostgreSQL healthcheck

## Docker Setup

The project uses Docker Compose to run the complete application stack together.

The Compose setup provides:

- Frontend container
- Backend container
- PostgreSQL container
- Shared Docker networking
- Persistent PostgreSQL storage
- Environment-based configuration
- Service dependency management
- Database healthcheck
- Backend healthcheck
- Nginx reverse proxy

The frontend is exposed on port `8080` on the host.

The backend listens on port `8080` inside its container and is accessed through Nginx rather than being required to be publicly exposed.

PostgreSQL listens on its standard container port `5432`.

## Docker Images

The frontend uses a multi-stage build:

- Builder: Docker Hardened Node.js development image
- Runner: Nginx Alpine image

The backend uses a multi-stage build:

- Builder: Docker Hardened Go Alpine image
- Runner: Docker Hardened Go Alpine image

Using multi-stage builds keeps build dependencies and source files out of the production frontend and keeps the backend runtime focused on the compiled application.

## Environment Configuration

Runtime configuration is kept in `.env` and is based on the provided `.env.example` template.

The main configuration values include:

- Frontend host port
- Backend port
- PostgreSQL username
- PostgreSQL password
- PostgreSQL database name
- PostgreSQL connection URL

The backend connects to PostgreSQL through the Docker Compose service name rather than `localhost`.

The PostgreSQL connection follows this structure:

`postgres://USERNAME:PASSWORD@DATABASE_SERVICE:5432/DATABASE?sslmode=disable`

This allows the backend container to communicate with the PostgreSQL container through Docker's internal network.

## Database Persistence

PostgreSQL data is stored in a named Docker volume so that removing and recreating containers does not automatically remove the database data.

The project also contains PostgreSQL initialization files under `init/postgres/`.

These scripts are used by PostgreSQL during the first initialization of a new database volume to create the required schema and load example data.

## API

The frontend communicates with the backend through the `/api/` path.

The backend provides endpoints for:

- Listing projects
- Creating projects
- Listing tasks for a project
- Creating tasks
- Updating tasks
- Searching tasks
- Backend health status

The browser communicates with the frontend through Nginx, while Nginx forwards API traffic to the backend over the Docker network.

## Healthchecks

Healthchecks are used to make the stack more reliable during startup.

### PostgreSQL

PostgreSQL readiness is checked using its built-in `pg_isready` utility.

### Backend

The Go API exposes a health endpoint that can be used to verify that the backend is running.

### Frontend

Nginx is configured as the production frontend server. A separate healthcheck is optional because successful Nginx startup provides a basic runtime check for this project.

## Running the Project

### Requirements

Only Docker with Docker Compose is required.

Node.js, Go, and PostgreSQL do not need to be installed locally because they run inside containers.

### Start

Create the local `.env` file from the example configuration and start the application with Docker Compose.

After the containers are running, open the frontend at:

`http://localhost:8080`

The backend health endpoint is available through the backend service for health verification.

### Stop

Stop the Compose stack when finished.

### Reset Database

The database can be reset by removing the PostgreSQL volume and starting the stack again. This causes the initialization scripts to run again and recreates the example database state.

## Folder Structure

- `docker-compose.yml` — runs the complete application stack
- `Makefile` — provides convenient project commands
- `.env.example` — environment configuration template
- `frontend/` — React/Vite frontend and Nginx configuration
- `backend/` — Go API and backend Dockerfile
- `init/postgres/` — PostgreSQL schema and seed initialization files
- `assets/` — project screenshots

## DevSecOps / CI/CD

The repository includes GitHub Actions workflows for:

- SonarQube static application security testing
- OWASP ZAP dynamic application security testing
- Docker image build and push automation

### SonarQube

A self-hosted SonarQube instance can be used for source-code analysis.

The GitHub Actions workflow uses repository configuration for the SonarQube host and authentication token.

### Docker Hub

The CI pipeline can build and push the application images to Docker Hub.

Docker Hub credentials should be stored as GitHub Actions secrets and variables rather than committed to the repository.

## What This Project Demonstrates

This project demonstrates a production-oriented containerized full-stack application with:

- React frontend
- Go REST API
- PostgreSQL database
- Docker multi-stage builds
- Docker Compose
- Docker networking
- Nginx reverse proxy
- API routing
- Persistent database volumes
- Environment-based configuration
- Container healthchecks
- Docker Hardened Images
- CI/CD security scanning
- Docker image publishing

## Application Screenshot

The screenshot below shows the DevBoard application running with real project and task data loaded from PostgreSQL.

![DevBoard running application](./assets/devboard.png)
