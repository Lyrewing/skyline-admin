import json, time, datetime
from flask import Blueprint, Response
from admin.models.user import User
from admin.libs.jwt import jwt_encode
from admin.libs.error import AuthFailed

token = Blueprint('token', __name__)


@token.route("/token", methods=['POST'])
def get_token():
    result = User.verify("feng", "123456")
    if result:
        iat = time.time()
        expire = (datetime.datetime.now() + datetime.timedelta(days=1)).timetuple()
        exp = time.mktime(expire)
        header = {
            'iss': 'http://example.com/',
            'sub': 'yosida95',
            'iat': iat,
            'exp': exp
        }
        payload = {
            'name': "John",
            'admin': True
        }

        token_key = jwt_encode(payload, header)
        try:
            token_data = {"data": token_key}
            response = json.dumps(token_data)
        except Exception as error:
            raise error
    else:
        return AuthFailed()
    return Response(response, mimetype="application/json")

