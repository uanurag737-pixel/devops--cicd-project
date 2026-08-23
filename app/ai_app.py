from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__)
@app.route("/")
def home():
    return send_from_directory(".", "ai.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    error_message = data.get("error", "").lower()

    if not error_message:
        return jsonify({"error": "Please provide an error message"}), 400

    if "crashloopbackoff" in error_message:
        analysis = """
1. What the error means:
The container is starting and then repeatedly crashing.

2. Possible root causes:
- Application error
- Wrong command or entrypoint
- Missing environment variable
- Port configuration issue
- Dependency failure

3. Troubleshooting steps:
Check pod details and container logs.

4. Useful commands:
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous

5. Recommended fix:
Identify the application error from logs, fix the configuration or application issue, rebuild the Docker image, and redeploy.
"""
    elif "imagepullbackoff" in error_message:
        analysis = """
1. What the error means:
Kubernetes cannot pull the container image.

2. Possible root causes:
- Wrong image name or tag
- Private registry authentication issue
- Image does not exist
- Registry connectivity problem

3. Useful commands:
kubectl describe pod <pod-name>
docker pull <image-name>
kubectl get pods

4. Recommended fix:
Verify the image name and tag, confirm the image exists in Docker Hub, and check registry credentials.
"""
    elif "docker" in error_message:
        analysis = """
Possible Docker issue detected.

Check:
docker ps -a
docker images
docker logs <container-name>
docker inspect <container-name>

Recommended fix:
Review the container logs, Dockerfile configuration, ports, and image build output.
"""
    elif "jenkins" in error_message:
        analysis = """
Possible Jenkins pipeline issue detected.

Check:
- Jenkins Console Output
- Credentials configuration
- Git branch configuration
- Docker availability inside Jenkins
- Pipeline syntax

Useful commands:
docker logs jenkins
docker exec jenkins docker --version
"""
    else:
        analysis = """
AI DevOps Demo Analysis

Possible troubleshooting steps:

1. Read the exact error message.
2. Check application and container logs.
3. Verify configuration files.
4. Confirm networking and credentials.
5. Check service health.

Useful commands:

kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
docker ps -a
docker logs <container-name>

This response is currently running in Demo AI Mode.
"""

    return jsonify({
        "analysis": analysis,
        "mode": "demo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)