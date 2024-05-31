#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# Sample user data stored in memory
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    """Route for the root URL"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Route to serve JSON data"""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Route to return OK status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Route to return user data by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Route to add a new user"""
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
