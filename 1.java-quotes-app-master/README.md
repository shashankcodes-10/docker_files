# Java Motivational Quotes App

## 👨‍💻 My Docker Observations

I containerized this Java-based motivational quotes application as part of my hands-on **Docker and DevOps learning**.

I experimented with different Java Docker images and also created a **multi-stage Docker build** to understand how the Java runtime and Docker build strategy affect the final image size.

### 🐳 Docker Image Size Comparison

| Build / Java Version | Docker Approach | Observed Image Size |
|---|---|---:|
| Java 21 | JDK-based image | **~554 MB** |
| Java 24 | JDK-based image | **~437 MB** |
| Java 25 | JDK-based image | **~420 MB** |
| Java 21 | Multi-stage: JDK builder + JRE runtime | **~285 MB** |

### 📊 My Observation

The multi-stage build produced an image of approximately **285 MB**.

Compared with the Java 21 JDK image I previously built at approximately **554 MB**, this reduced the image by around:

> **📉 ~269 MB (~48.6% smaller)**

The reduction comes mainly from using a **JDK in the builder stage** and a **JRE in the final runtime stage**.

However, the multi-stage image is not necessarily the smallest image possible. The final image still contains the Java 21 JRE and its underlying Alpine runtime. The exact size can also vary depending on the architecture, Docker version, base-image updates, cached layers, and how Docker reports image size.

### 💡 Key Docker Takeaway

> **The build environment does not need to be the runtime environment.**

The JDK is required for:

```text
javac → compile Main.java
```

but the running application only needs:

```text
java → run Main.class
```

Therefore, using a JDK for the build stage and a JRE for the production stage avoids carrying the compiler and other JDK tooling into the final runtime image.

---

## 🖥️ Application Output

The application starts an HTTP server on port `8000` and returns a random motivational quote in JSON format.

![Java Quotes App Output](./Screenshot.png)

Example endpoint:

```text
http://localhost:8000/
```

Example response:

```json
{
  "quote": "Your motivational quote appears here"
}
```

---

## 🔗 Docker Hub

The Docker image is available on Docker Hub:

**[🐳 https://hub.docker.com/repository/docker/shashank971/java-quotes-app/general](https://hub.docker.com/repository/docker/shashank971/java-quotes-app/general)**

Pull the image:

```bash
docker pull shashank971/java-quotes-app:latest
```

Run the application:

```bash
docker run -p 8000:8000 shashank971/java-quotes-app:latest
```

Then open:

```text
http://localhost:8000/
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Java |
| Java Runtime | Eclipse Temurin |
| Java Version Tested | 21, 24, 25 |
| HTTP Server | `com.sun.net.httpserver.HttpServer` |
| Containerization | Docker |
| Base Image | Eclipse Temurin Alpine |
| Runtime Port | 8000 |

---

## ✨ Features

- Lightweight Java HTTP server
- Returns random motivational quotes
- Quotes stored in an external `quotes.txt` file
- JSON API response
- Dockerized application
- Single-stage Docker build
- Multi-stage Docker build
- JDK → JRE runtime optimization

---

## 📁 Project Structure

```text
java-quotes-app/
├── src/
│   └── Main.java          # Java HTTP server
├── quotes.txt             # Motivational quotes
├── Dockerfile             # Single-stage Docker build
├── Dockerfile.multistage  # Multi-stage JDK → JRE build
├── Screenshot.png         # Application output screenshot
└── README.md              # Project documentation
```

---

## ⚙️ How the Application Works

The application uses Java's built-in:

```text
com.sun.net.httpserver.HttpServer
```

to create a lightweight HTTP server.

The application:

1. Loads quotes from `quotes.txt`.
2. Starts an HTTP server on port `8000`.
3. Creates an endpoint at `/`.
4. Selects a random quote.
5. Returns the quote as a JSON response.

The basic flow is:

```text
quotes.txt
    ↓
Main.java
    ↓
Java HTTP Server
    ↓
GET /
    ↓
Random Quote
    ↓
JSON Response
```

---

## 🚀 Running Locally

Compile the application:

```bash
javac src/Main.java -d out
```

Run it:

```bash
java -cp out Main
```

The server will start on:

```text
http://localhost:8000
```

Test it with:

```bash
curl http://localhost:8000/
```

---

## 🐳 Docker Usage

### Single-stage build

Build:

```bash
docker build -t java-quotes-app .
```

Run:

```bash
docker run -p 8000:8000 java-quotes-app
```

### Multi-stage build

Build:

```bash
docker build -f Dockerfile.multistage -t java-quotes-app:multistage .
```

Run:

```bash
docker run -p 8000:8000 java-quotes-app:multistage
```

---

## 📈 Docker Image Optimization

The multi-stage Dockerfile follows this approach:

```text
                 Build Stage
                     │
          Eclipse Temurin JDK
                     │
                javac Main.java
                     │
                     ▼
                Main.class
                     │
                     ▼
              Runtime Stage
                     │
          Eclipse Temurin JRE
                     │
                     ▼
             Final Container
```

The compiler and other JDK tooling are needed only during the build stage.

The final application only needs the Java runtime to execute `Main.class`.

This is why a **JDK → JRE multi-stage build** can significantly reduce the runtime image compared with keeping the complete JDK in the final container.

---

## 📌 Experiment Summary

| Experiment | Result |
|---|---:|
| Java 21 JDK image | ~554 MB |
| Java 24 JDK image | ~437 MB |
| Java 25 JDK image | ~420 MB |
| Java 21 JDK → JRE multi-stage | **~285 MB** |

This experiment helped me understand that Docker image optimization involves more than just choosing a Java version.

Important factors include:

- JDK vs JRE
- Base image
- Multi-stage builds
- Architecture
- Application dependencies
- Build artifacts
- Runtime requirements

---

##  Original Project / Author

This project was originally taken from **Shubham Londhe / TrainWithShubham**.

**Author / source repository:**

https://github.com/LondheShubham153

The Dockerization, Java-version image-size experiments, multi-stage Docker build, and observations documented above are my own hands-on work.
