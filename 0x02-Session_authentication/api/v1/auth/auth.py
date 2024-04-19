#!/usr/bin/env python3
"""
Authentication class
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False if path is in the list
        of excluded paths. ie: path does not
        require authentication
        """
        if path and excluded_paths:
            for excluded_path in excluded_paths:
                if excluded_path[-1] == "*":
                    excluded_path, discard = excluded_path.split('*')
                    if excluded_path in path:
                        return False
            if path[-1] != '/':
                path += '/'
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns Authorization header if present
        in request
        Otherwise, returns None
        """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header:
            # print(f"auth_header: {auth_header}")
            return auth_header
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user function
        """
        return None
    
    def session_cookie(self, request=None):
        """ session_cookie
        """
        if request:
            session_name = getenv("SESSION_NAME")
            return request.cookies.get(session_name, None)
