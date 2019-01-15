# 与用户业务相关的操作
# 如:用户的注册,登录,登出,...
from flask import Blueprint

user = Blueprint('user', __name__)
from . import views
