#!/usr/bin/env python3
"""
Password encryption module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted hashed password
    using bcrypt
    """
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """  
    Checks the validity of the hashed_password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
