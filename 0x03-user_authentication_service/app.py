#!/usr/bin/env python3
"""
Main file
"""
from flask import Flask, jsonify, request, abort, redirect
from flask.helpers import make_response
from auth import Auth
from db import DB
from user import User


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    """GET /
    Returns welcome message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main___":
    app.run(host="0.0.0.0", port="5000")
