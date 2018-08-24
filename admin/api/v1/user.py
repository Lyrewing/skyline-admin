import json
from flask import Blueprint, Response, request
from admin.models.user import User
from admin.api.v1.form import RegisterUserForm
from admin.libs.error import ParameterException, Success
from flask_httpauth import HTTPTokenAuth
from admin.libs.jwt import jwt_decode

user = Blueprint("user", __name__)
auth = HTTPTokenAuth(scheme='Bearer')


@user.route("/get")
@auth.login_required
def get_user():
    users = User.get_all_user()
    response = json.dumps(users)
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


@user.route("/register", methods=['POST'])
def register():
    form = RegisterUserForm(csrf_enabled=False)
    if form.validate_on_submit():
        account = request.form['account']
        password = request.form['password']
        User.register_by_email(account, password)
        return Success()
    else:
        return ParameterException()


@auth.verify_token
def verify_token(token):
    if token:
        try:
            payload = jwt_decode(token)
            return True
        except Exception as error:
            return False
