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


@app.route('/')
def home():
    """Route for the root URL"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Route to serve JSON data"""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Route to return OK status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Route to return user data by username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Route to add a new user"""
    data = request.json
    username = data.get('username')
    if username:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201
    else:
        return jsonify({"error": "Username not provided"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
