# DevBoard — React + Vite Frontend

## 👨‍💻 My Docker Observations

I containerized this DevBoard frontend as part of my hands-on **Docker and DevOps learning**.

During the process, I experimented with both a **single-stage Docker build** and a **multi-stage Docker build** to understand their impact on the final image size.

## 🐳 Docker Image Size Comparison

| Docker Build | Image                                | Observed Size |
| ------------ | ------------------------------------ | ------------: |
| Single-stage | `shashank971/devboard-ui:latest`     |   **~735 MB** |
| Multi-stage  | `shashank971/devboard-ui:multistage` |    **~93 MB** |

### 📊 Result

The multi-stage Docker build reduced the image size from approximately **735 MB to 93 MB**.

That's a reduction of approximately:

> **📉 ~642 MB / ~87.3% smaller**

This experiment demonstrated an important Docker optimization principle:

> **The build environment doesn't need to be the runtime environment.**

The single-stage image contains the Node.js environment, npm dependencies, source code, and development tooling.

With the multi-stage approach, the application is built in a Node.js environment and only the required production files are included in the final runtime image.

### 🖥️ Application Output

The DevBoard application was successfully built and run through Docker.

![DevBoard Application Output](./devboard-output.png)

The screenshot shows the DevBoard dashboard with:

* Workspace overview
* Project velocity
* Task status cards
* Projects section
* Recent tasks
* Dark-themed dashboard UI


### 🔗 Docker Hub Images

**Single-stage image:**
[🐳 `shashank971/devboard-ui:latest`](https://hub.docker.com/repository/docker/shashank971/devboard-ui/general)

**Multi-stage image:**
[🐳 `shashank971/devboard-ui:multistage`](https://hub.docker.com/repository/docker/shashank971/devboard-ui/general)

You can pull the images using:

```bash
docker pull shashank971/devboard-ui:latest
```

```bash
docker pull shashank971/devboard-ui:multistage
```


---

## 🚀 Running the Docker Images

### Single-stage image

```bash
docker run -p 5173:5173 shashank971/devboard-ui:latest
```

### Multi-stage image

```bash
docker run -p 5173:5173 shashank971/devboard-ui:multistage
```

Then open:

```text
http://localhost:5173
```

> **Note:** The image sizes mentioned above are the sizes I observed during my builds. Actual sizes can vary depending on the base image version, architecture, dependency versions, and Docker configuration.

---

# Project Overview

DevBoard is a modern task and project management frontend built with React and Vite. It provides a dashboard-style interface for viewing projects, tasks, progress, and task statuses.

## ✨ Features

* Modern DevBoard dashboard UI
* Project overview
* Task management interface
* Kanban board components
* Task creation modal
* Project detail pages
* Search/command bar
* Theme toggle
* Responsive layout
* API integration through a small `fetch` wrapper
* React Router based navigation
* React Query for server-state management
* Component tests using Vitest and Testing Library

## 🛠️ Tech Stack

| Component     | Technology               |
| ------------- | ------------------------ |
| Frontend      | React 18                 |
| Build Tool    | Vite                     |
| Runtime       | Node.js 22               |
| Styling       | Tailwind CSS             |
| Routing       | React Router             |
| Data Fetching | TanStack React Query     |
| Icons         | Tabler Icons             |
| Testing       | Vitest + Testing Library |
| Container     | Docker                   |
| Base Image    | `node:22-alpine`         |

## 📁 Project Structure

```text
devboard-ui/
├── public/
├── src/
│   ├── api/
│   │   └── client.js
│   ├── components/
│   │   ├── layout/
│   │   ├── tasks/
│   │   └── ui/
│   ├── hooks/
│   │   └── useTasks.js
│   ├── pages/
│   │   ├── DashboardPage.jsx
│   │   └── ProjectPage.jsx
│   ├── styles/
│   ├── test/
│   ├── App.jsx
│   └── main.jsx
├── .dockerignore
├── Dockerfile
├── Dockerfile-multi
├── package.json
├── package-lock.json
├── tailwind.config.js
├── vite.config.js
└── index.html
```

## ⚙️ Local Development

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The application runs on:

```text
http://localhost:5173
```

## 🧪 Testing

Run the test suite with:

```bash
npm test
```

## 🔍 Linting

Run ESLint with:

```bash
npm run lint
```

## 🔗 API / Backend

The frontend contains an API client and Vite proxy configuration for communicating with a Go backend.

For local development, `/api` requests are proxied to:

```text
http://localhost:8080
```

For Vite preview/Compose usage, the proxy is configured to communicate with a backend service named:

```text
backend:8080
```

## 📌 Docker Learning Takeaway

This project demonstrated the significant impact that **multi-stage Docker builds** can have on image size.

### Before

**Single-stage: ~735 MB**

### After

**Multi-stage: ~93 MB**

That's approximately an **87.3% reduction** in image size.

The main reason for this reduction is that the final image does not need the complete Node.js development environment, npm tooling, and build-time dependencies.

The application is built in one stage, and only the required production files are carried into the final runtime image.

### Key Takeaway

> **Build with a full environment, but run with only what the application needs.**

Multi-stage builds are therefore an effective way to reduce Docker image size, improve security, and minimize unnecessary components in production containers.

---

# Original Project / Author

This project was originally taken from **Shubham Londhe**.

**Author / source repository:**

https://github.com/LondheShubham153

The Dockerization, multi-stage optimization, image-size comparison, and observations in this README are my own hands-on work.
