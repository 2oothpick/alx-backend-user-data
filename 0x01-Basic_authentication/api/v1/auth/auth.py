#!/usr/bin/env python3
"""
Authentication class
"""

from flask import request
from typing import List, TypeVar


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
                if excluded_path[-1] is "*":
                    excluded_path, discard = excluded_path.split('*')
                    if excluded_path in path:
                        return False
            if path[-1] is not '/':
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
