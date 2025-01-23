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
