import json, time, datetime
from flask import Blueprint, Response, request
from admin.models.user import User
from admin.libs.jwt import jwt_encode, jwt_decode
from admin.libs.error import AuthFailed, Success, ServerException
from flask_httpauth import HTTPBasicAuth

token = Blueprint('token', __name__)
auth = HTTPBasicAuth()


@token.route("/token", methods=['POST'])
@auth.login_required
def get_token():
    iat = time.time()
    expire = (datetime.datetime.now() + datetime.timedelta(minutes=20)).timetuple()
    exp = time.mktime(expire)
    header = {
        "alg": "RS256",
        "typ": "JWT"
    }
    payload = {
        'iss': 'http://example.com/',
        'sub': 'yosida95',
        'iat': iat,
        'exp': exp,
        'name': "John",
        'admin': True
    }

    token_key = jwt_encode(payload, header)
    try:
        token_data = {"data": token_key}
        response = json.dumps(token_data)
        return Response(response, mimetype="application/json")
    except Exception as error:
        return ServerException(error)


@token.route("/check", methods=['POST'])
def verify_token():
    token_value = request.json['token']
    if token_value:
        try:
            payload = jwt_decode(token_value)
            flg = True
        except Exception as error:
            flg = False
        result = json.dumps({'result': flg})
        return Response(result, mimetype="application/json")


@auth.verify_password
def verify_password(username, password):
    result = User.verify(email=username, secret=password)
    return result
