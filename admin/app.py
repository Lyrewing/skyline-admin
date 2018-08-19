from admin import app
from admin.routes import register_blueprints
from admin.libs.error import ApiException
from werkzeug.exceptions import HTTPException

# 注册的路由
register_blueprints()


@app.errorhandler(Exception)
def framwork_error(e) -> ApiException:
    if isinstance(e, ApiException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = -2
        return ApiException(msg, code, error_code)
    else:
        return ApiException()


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5555)
