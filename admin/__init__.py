from flask import Flask
from admin.config import DevConfig

app = Flask(__name__)
# 设置环境配置
app.config.from_object(DevConfig)
