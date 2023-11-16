#!/usr/bin/env python3
""" User module """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence


Base = declarative_base()


class User(Base):
    """User Model"""
    __tablename__ = 'users'

    hashed_password = Column(String(250), Sequence('user_id_seq'), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)
