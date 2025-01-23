#!/usr/bin/env python3
"""
Password encryption module
"""
from bcrypt import hashpw, gensalt, checkpw


def hash_password(password: str) -> bytes:
    """
    Returns a salted hashed password
    using bcrypt
    """
    salt = gensalt()
    hash = hashpw(password.encode('utf-8'), salt)
    return salt
