from admin import app
from admin.routes import register_blueprints

# 注册的路由
register_blueprints()

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5555)
