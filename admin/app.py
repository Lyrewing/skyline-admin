from admin.libs.error import ApiException
from werkzeug.exceptions import HTTPException
from flask import Flask
from admin.config import DevConfig
from admin.api.v1.book import book
from admin.api.v1.user import user
from admin.api.v1.token import token


app = Flask(__name__)
# 设置环境配置
app.config.from_object(DevConfig)
# 注册的路由
app.register_blueprint(user, url_prefix="/v1/user")
app.register_blueprint(book, url_prefix="/v1/book")
app.register_blueprint(token, url_prefix="/v1/token")

#全局异常过滤器
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

