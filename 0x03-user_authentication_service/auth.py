#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from db import DB
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
