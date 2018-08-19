import json
from flask import Blueprint, Response
from admin.models.user import User
from admin.libs.authorize import authorize

user = Blueprint("user", __name__)


@user.route("/get")
def get_user():
    return "get user"


@user.route("/login", methods=['POST'])
def login():
    result = User.verify("feng", "123456")
    response = json.dumps({"data": result})
    return Response(response, mimetype="application/json")


@user.route("/add", methods=['POST'])
@authorize
def add_user():
    User.register_by_email("feng", "123456")
    _user = {'name': 'feng', 'age': 18}
    result = json.dumps(_user)
    return Response(result, mimetype="application/json")
