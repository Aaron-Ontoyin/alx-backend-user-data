#!/usr/bin/env python3
import requests

"""
Main file
Test module: end to end integration test
"""


def register_user(email: str, password: str) -> None:
    """Test for register user"""
    data = {"email": email, "password": password}
    response = requests.post("http://localhost:5000/users", json=data)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """Test for login with wrong password"""
    data = {"email": email, "password": password}
    response = requests.post("http://localhost:5000/sessions", json=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test for login"""
    data = {"email": email, "password": password}
    response = requests.post("http://localhost:5000/sessions", json=data)
    assert response.status_code == 200


def profile_unlogged() -> None:
    """Test for profile unlogged"""
    response = requests.get("http://localhost:5000/profile")
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test for profile logged"""
    response = requests.get("http://localhost:5000/profile")
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """Test for logout"""
    response = requests.delete("http://localhost:5000/sessions")
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """Test for reset password"""
    response = requests.post(
        "http://localhost:5000/reset_password",
        json=email,
    )
    assert response.status_code == 200


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test for update password"""
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }
    response = requests.put("http://localhost:5000/reset_password", json=data)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
