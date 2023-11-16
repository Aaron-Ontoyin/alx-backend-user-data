#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt


def _hash_password(self, password: str) -> bytes:
    """Return a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
