# main:处理与博客相关的业务逻辑们
# 如:发表博客,查看博客,删除博客,...
# 将自己加入到Blueprint中
from flask import Blueprint

main = Blueprint("main", __name__)
from . import views
