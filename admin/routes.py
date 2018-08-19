from admin import app
from admin.api.v1.book import book
from admin.api.v1.user import user
from admin.api.v1.token import token


def register_blueprints():
    app.register_blueprint(user, url_prefix="/v1/user")
    app.register_blueprint(book, url_prefix="/v1/book")
    app.register_blueprint(token, url_prefix="/v1/token")
