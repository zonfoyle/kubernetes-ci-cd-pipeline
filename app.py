from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Kubernetes CI/CD Flask API")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from the Kubernetes CI/CD pipeline project",
        "app": APP_NAME,
        "environment": ENVIRONMENT
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)