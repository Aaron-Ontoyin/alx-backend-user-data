#!/usr/bin/env python3
"""
Main file
"""
from flask import Flask, jsonify, request, abort, redirect
from flask.helpers import make_response
from auth import Auth
from db import DB
from user import User


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """GET /
    Returns welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    """User registration end-point"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main___":
    app.run(host="0.0.0.0", port="5000")
