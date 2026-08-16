# Java Motivational Quotes App

## 👨‍💻 My Docker Observations

I containerized this Java-based motivational quotes application as part of my hands-on **Docker and DevOps learning**.

I experimented with different Java versions, **multi-stage Docker builds**, and a **Distroless Java runtime** to understand how the Java runtime and Docker build strategy affect the final image size.

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

**[🐳 Docker Hub Repository](https://hub.docker.com/repository/docker/shashank971/java-quotes-app/general)**

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

### 🐳 Docker Image Size Comparison

| Build / Java Version | Docker Approach | Observed Image Size |
|---|---|---:|
| Java 21 | JDK-based image | **~554 MB** |
| Java 24 | JDK-based image | **~437 MB** |
| Java 25 | JDK-based image | **~420 MB** |
| Java 21 | Multi-stage: JDK builder + JRE runtime | **~285 MB** |
| Java 21 | Multi-stage: JDK builder + Distroless Java runtime | **~261 MB** |

---

## 📊 My Observation

The biggest reduction came from moving from a **JDK-based runtime image** to a **JRE-based runtime**.

```text
Java 21 JDK
~554 MB
    ↓
Java 21 JRE
~285 MB
    ↓
Java 21 Distroless
~261 MB
```

### JDK → JRE

The multi-stage JDK → JRE build reduced the image from approximately:

> **554 MB → 285 MB**

That's a reduction of approximately:

> **📉 269 MB (~48.6% smaller)**

The main reason is that the final image no longer contains the JDK compiler and development tooling.

### JRE → Distroless

Replacing the JRE Alpine runtime with a Distroless Java runtime further reduced the image from:

> **285 MB → 261 MB**

That's an additional reduction of approximately:

> **📉 24 MB (~8.4%)**

### Overall reduction

Compared with the original Java 21 JDK image:

> **554 MB → 261 MB**

That's an overall reduction of approximately:

> **📉 293 MB (~52.9% smaller)**

This experiment showed me that **the biggest size optimization came from JDK → JRE**, while Distroless provided an additional reduction along with a more minimal production runtime.

---

## 🧊 Distroless Experiment

I also created a **multi-stage Docker build using a Distroless Java runtime**.

The architecture is:

```text
                 Build Stage
                     │
          Eclipse Temurin JDK 21
                     │
                 javac Main.java
                     │
                 Main.class
                     │
                  app.jar
                     │
                     ▼
              Production Stage
                     │
          Distroless Java 21
                     │
                     ▼
                   app.jar
                     │
                     ▼
              Running Application
```

The Distroless image produced an observed size of:

> **~261 MB**

The Distroless runtime removes many unnecessary components that are not required to run the Java application, such as:

- Shell
- Package manager
- Unnecessary OS utilities
- Development tools

This provides a more minimal production runtime and can also reduce the attack surface.

> **Key takeaway:** Distroless does not always produce a massive size reduction. In this experiment, the major reduction came from **JDK → JRE**, while **JRE → Distroless** provided an additional ~24 MB reduction.

---

## 💡 Key Docker Takeaway

> **The build environment does not need to be the runtime environment.**

The JDK is required for:

```text
javac → compile Main.java
```

but the running application only needs:

```text
java → run app.jar
```

Therefore:

```text
JDK
 ↓
Build application
 ↓
JRE / Distroless Java
 ↓
Run application
```

allows unnecessary build tools to stay outside the final production image.

---



## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Java |
| Java Runtime | Eclipse Temurin |
| Java Versions Tested | 21, 24, 25 |
| HTTP Server | `com.sun.net.httpserver.HttpServer` |
| Containerization | Docker |
| Base Image | Eclipse Temurin Alpine |
| Production Runtime | JRE / Distroless Java |
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
- JDK → Distroless runtime optimization
- Docker image-size comparison

---

## 📁 Project Structure

```text
java-quotes-app/
├── src/
│   └── Main.java             # Java HTTP server
├── quotes.txt                # Motivational quotes
├── Dockerfile                # Single-stage Docker build
├── Dockerfile.multistage     # Multi-stage JDK → JRE build
├── Dockerfile.distroless     # Multi-stage JDK → Distroless build
├── Screenshot.png            # Application output screenshot
└── README.md                 # Project documentation
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

# 🐳 Docker Usage

## Single-stage Build

Build:

```bash
docker build -t java-quotes-app .
```

Run:

```bash
docker run -p 8000:8000 java-quotes-app
```

---

## Multi-stage Build

Build:

```bash
docker build -f Dockerfile.multistage -t java-quotes-app:multistage .
```

Run:

```bash
docker run -p 8000:8000 java-quotes-app:multistage
```

---

## Distroless Build

Build:

```bash
docker build -f Dockerfile.distroless -t java-quotes-app:distroless .
```

Run:

```bash
docker run -p 8000:8000 java-quotes-app:distroless
```

---

# 📈 Docker Image Optimization

The Docker optimization progression was:

```text
                 Single-stage
                      │
               Eclipse Temurin
                  JDK 21
                      │
                      ▼
                  ~554 MB
                      │
                      │ Multi-stage
                      ▼
               JDK 21 → JRE 21
                      │
                      ▼
                  ~285 MB
                      │
                      │ Distroless
                      ▼
          JDK 21 → Distroless Java 21
                      │
                      ▼
                  ~261 MB
```

### Size comparison

```text
Java 21 JDK          ~554 MB
████████████████████████████████████████████

Java 21 JRE          ~285 MB
█████████████████████

Java 21 Distroless   ~261 MB
███████████████████
```

### What the experiment demonstrated

**JDK → JRE:**

```text
~554 MB → ~285 MB
```

**JRE → Distroless:**

```text
~285 MB → ~261 MB
```

**Overall:**

```text
~554 MB → ~261 MB
```

Therefore, the total reduction was approximately:

> **📉 293 MB (~52.9%)**

---

## 📌 Experiment Summary

| Experiment | Observed Size | Main Learning |
|---|---:|---|
| Java 21 JDK | **~554 MB** | Full development runtime |
| Java 24 JDK | **~437 MB** | Base image/version affects size |
| Java 25 JDK | **~420 MB** | Base image/version affects size |
| Java 21 JDK → JRE | **~285 MB** | Remove build-time JDK tooling |
| Java 21 JDK → Distroless | **~261 MB** | Minimal production runtime |

### Final Docker Learning

This experiment helped me understand that Docker image optimization involves more than simply choosing a newer Java version.

Important factors include:

- JDK vs JRE
- Distroless vs traditional runtime images
- Multi-stage builds
- Base image selection
- Application dependencies
- Build artifacts
- Runtime requirements
- Container architecture

> **Final takeaway:** The biggest optimization in this project came from separating the **JDK build environment from the production runtime**. Distroless provided an additional reduction and a more minimal runtime, but the goal of Distroless is not only image size — it is also reducing unnecessary components and the runtime attack surface.

---

## Original Project / Author

This project was originally taken from **Shubham Londhe / TrainWithShubham**.

**Author / source repository:**

https://github.com/LondheShubham153

The Dockerization, Java-version image-size experiments, multi-stage Docker build, Distroless experimentation, and observations documented above are my own hands-on work.
