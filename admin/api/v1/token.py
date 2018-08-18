import json
from flask import Blueprint, Response
from admin.models.user import User

token=Blueprint('token',__name__)

@token.route("/token", methods=['POST'])
def get_token():
    result = User.verify("feng", "123456")
    if result:
        token=""
    response = json.dumps({"data": token})
    return Response(response, mimetype="application/json")
    pass