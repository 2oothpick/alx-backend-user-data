#!/usr/bin/env python3
"""
Module for BasicAuthentication class
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class
    inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the string after "Basic "
        """
        if authorization_header and type(authorization_header) == str:
            if authorization_header[:6] == 'Basic ':
                return authorization_header[6:]
        return None

    def decode_base64_authorization_header(self,
                                           encoded_string: str) -> str:
        """
        decodes base64 authorization header
        """
        if encoded_string and type(encoded_string) == str:
            try:
                encode = encoded_string.encode('utf-8')
                decoded = base64.b64decode(encode)
            except Exception as e:
                return None
            else:
                return decoded.decode('utf-8')
        return None

    def extract_user_credentials(self, db64_auth_header: str) -> (str, str):
        """
        Extracts user credentials from provided
        decoded_base64_authorization_header
        """
        if db64_auth_header and type(db64_auth_header) == str:
            if ":" in db64_auth_header:
                email, paswrd = db64_auth_header.split(':', maxsplit=1)
                return (email, paswrd)
        return (None, None)

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        """
        Returns user object from credentials
        """
        if user_email and user_pwd:
            if type(user_email) == str and type(user_pwd) == str:
                user = None
                try:
                    user = User.search({'email': user_email})
                except Exception:
                    return
                else:
                    for obj in user:
                        if obj.is_valid_password(user_pwd):
                            return obj
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from the
        request header
        """
        auth_header = self.authorization_header(request)
        b64_auth_header = self.extract_base64_authorization_header(auth_header)
        db64_auth_header = self.decode_base64_authorization_header(
            b64_auth_header)
        email, pwd = self.extract_user_credentials(db64_auth_header)
        return self.user_object_from_credentials(email, pwd)
