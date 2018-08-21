import json
from flask import Blueprint, Response
from admin.models.user import User
from flask_httpauth import HTTPBasicAuth
from admin.libs.json import AlchemyEncoder
user = Blueprint("user", __name__)
auth = HTTPBasicAuth()


@user.route("/get")
@auth.login_required
def get_user():
    users = User.get_all_user()
    response = json.dumps(users,cls=AlchemyEncoder)
    return Response(response, mimetype="application/json")


@user.route("/login", methods=['POST'])
def login():
    result = User.verify("feng", "123456")
    response = json.dumps({"data": result})
    return Response(response, mimetype="application/json")


@user.route("/add", methods=['POST'])
def add_user():
    User.register_by_email("feng", "123456")
    _user = {'name': 'feng', 'age': 18}
    result = json.dumps(_user)
    return Response(result, mimetype="application/json")


@auth.verify_password
def verify_password(username, password):
    result = User.verify(name=username, secret=password)
    return result
