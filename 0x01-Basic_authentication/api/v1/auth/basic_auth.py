#!/usr/bin/env python3
"""
Module for BasicAuthentication class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header and type(authorization_header) == str:
            if authorization_header[:6] == 'Basic ':
                return authorization_header[7:]
        return None
