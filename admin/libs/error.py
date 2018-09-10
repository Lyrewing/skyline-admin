import json
from werkzeug.exceptions import HTTPException
from flask import request


class ApiException(HTTPException):
    code = 500
    msg = 'sorry have a mistake'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(ApiException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [("Content-type", "application/json")]

    @staticmethod
    def get_url():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]


class Success(ApiException):
    code = 200
    msg = 'ok'
    error_code = 0


class ClientTypeException(ApiException):
    code = 400
    error_code = 1006
    msg = "client is invalid"
    description = (
        'bad request'
    )


class AuthFailed(ApiException):
    code = 401
    error_code = 1000
    msg = "Authorized failed"


class ParameterException(ApiException):
    code = 400
    error_code = 10001
    msg = "Parameter error"


class ServerException(ApiException):
    code = 500
    error_code = 10005
    msg = "server error"
