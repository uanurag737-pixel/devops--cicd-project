# 🤖 AI DevOps Troubleshooting Assistant with CI/CD

An end-to-end DevOps project that combines a Flask-based troubleshooting assistant with Docker, Jenkins, Docker Hub, and Kubernetes.

The project demonstrates how an application can move automatically from source code to a containerized Kubernetes deployment through a CI/CD pipeline.

---

## 🚀 Project Overview

The AI DevOps Troubleshooting Assistant helps analyze common DevOps errors related to:

- Kubernetes
- Docker
- Jenkins
- Linux

The application currently runs in **Demo AI Mode**, where predefined troubleshooting logic provides explanations, useful commands, possible root causes, and recommended fixes for common DevOps errors.

Example:

```text
Kubernetes pod is in CrashLoopBackOff
```

The assistant provides troubleshooting guidance including commands such as:

```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
```

---

## 🏗️ CI/CD Architecture

```text
Developer
   ↓
GitHub Repository
   ↓
Jenkins Pipeline
   ↓
Docker Image Build
   ↓
Docker Hub
   ↓
Kubernetes Deployment
   ↓
AI DevOps Troubleshooting Assistant
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Git | Version Control |
| GitHub | Source Code Repository |
| Python | Backend Development |
| Flask | Web Application |
| HTML/CSS/JavaScript | Frontend |
| Docker | Application Containerization |
| Docker Hub | Container Image Registry |
| Jenkins | CI/CD Automation |
| Kubernetes | Container Orchestration |
| Minikube | Local Kubernetes Cluster |
| kubectl | Kubernetes Management |

---

## ⚙️ CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Checkout** — Pulls the latest source code from GitHub.
2. **Build Docker Image** — Builds a new Docker image using the project Dockerfile.
3. **Test** — Verifies that the Docker image was created successfully.
4. **Docker Hub Push** — Tags and pushes the image to Docker Hub.
5. **Deploy to Kubernetes** — Updates the Kubernetes Deployment with the newly built image.
6. **Rollout Status** — Verifies that the Kubernetes rollout completes successfully.
7. **Verify Pods** — Confirms that the application pods are running.

---

## 🐳 Docker

The Flask application is packaged inside a Docker container.

Example build:

```bash
docker build -t devops-cicd:v1 .
```

The application runs on:

```text
Port 5000
```

---

## ☸️ Kubernetes Deployment

The application is deployed to Kubernetes using a Deployment and NodePort Service.

The Kubernetes Deployment maintains:

```text
2 replicas
```

Application traffic flows through:

```text
Browser
   ↓
NodePort Service
   ↓
Service Port 80
   ↓
Target Port 5000
   ↓
Flask Application
```

---

## 🧠 Troubleshooting Features

The assistant currently recognizes common scenarios such as:

### CrashLoopBackOff

Provides possible causes including:

- Application errors
- Incorrect command or entrypoint
- Missing environment variables
- Dependency failures
- Port configuration issues

### ImagePullBackOff

Checks for problems such as:

- Incorrect Docker image name
- Incorrect image tag
- Missing image
- Private registry authentication
- Registry connectivity

### Docker Issues

Suggests useful troubleshooting commands including:

```bash
docker ps -a
docker images
docker logs <container-name>
docker inspect <container-name>
```

### Jenkins Issues

Helps investigate:

- Jenkins console output
- Credentials
- Git configuration
- Docker availability
- Pipeline syntax

---

## 📂 Project Structure

```text
devops-CICD-project/
│
├── app/
│   ├── ai_app.py
│   ├── ai.html
│   ├── index.html
│   ├── requirements.txt
│   │
│   └── k8s/
│       ├── deployment.yaml
│       └── service.yaml
│
├── Dockerfile
├── .gitignore
└── README.md
```

---

## 🎯 What I Learned

Through this project I gained hands-on experience with:

- Building Docker images
- Creating Jenkins CI/CD pipelines
- Using Jenkins credentials securely
- Pushing versioned images to Docker Hub
- Deploying applications to Kubernetes
- Working with Kubernetes Deployments and Services
- Troubleshooting Docker socket permissions
- Troubleshooting Kubernetes networking and port mappings
- Debugging CI/CD pipeline failures
- Integrating a Flask application into a DevOps workflow

---

## 🔮 Future Improvements

Future versions of this project can include:

- Live AI API integration
- Dynamic analysis of DevOps errors
- Automated testing in the Jenkins pipeline
- Kubernetes health checks
- Cloud deployment using AWS
- Monitoring with Prometheus and Grafana
- Production WSGI server for the Flask application

---

## 👨‍💻 Author

**Anurag Upadhyay**

DevOps / Cloud Enthusiast

Building hands-on projects with:

`Linux` • `Git` • `GitHub` • `Docker` • `Jenkins` • `Kubernetes` • `AWS`