from flask import request
from admin.libs.error import AuthFailed
from admin.libs.jwt import jwt_decode


def authorize(func):
    def wrapper(*args, **kwargs):
        """Token 验证"""
        auth = request.headers.get('Authorization')
        if not auth:
            return AuthFailed()
        elif auth:
            try:
                payload = jwt_decode(auth)
                func()
            except Exception as error:
                return AuthFailed()
        else:
            return AuthFailed()

    return wrapper


def login_required():
    pass
