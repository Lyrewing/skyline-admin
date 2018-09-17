from admin.libs.error import ApiException
from werkzeug.exceptions import HTTPException
from flask import Flask
from admin.config import DevConfig
from admin.api.v1.user import user
from admin.api.v1.token import token
from vote.api.votes import votes
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
# 设置环境配置
app.config.from_object(DevConfig)

# 注册的路由
app.register_blueprint(user, url_prefix="/v1/user")
app.register_blueprint(token, url_prefix="/v1/token")
app.register_blueprint(votes,url_prefix="/v1/vote")


# 全局异常过滤器
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
    app.run(host='localhost', port=5000)
