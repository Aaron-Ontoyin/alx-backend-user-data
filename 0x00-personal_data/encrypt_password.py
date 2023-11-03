#!/usr/bin/env python3
"""This module returns a hashed password, byte in string """
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns byte string password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validates provided password matches hashed_password
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
