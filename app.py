from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

messages = []  # Temporary in-memory storage

@app.route("/")
def home():
    return "Render Flask Server is running!"

@app.route("/send", methods=["POST"])
def send_message():
    try:
        data = request.get_json()
        username = data.get("username", "Unknown")
        message = data.get("message", "")

        entry = {
            "username": username,
            "message": message,
            "time": datetime.utcnow().isoformat()
        }
        messages.append(entry)

        return jsonify({"success": True, "stored": entry}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/get", methods=["GET"])
def get_messages():
    return jsonify(messages), 200
