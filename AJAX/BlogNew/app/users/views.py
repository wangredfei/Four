# 与users业务相关的路由和视图处理函数
from . import user


@user.route('/users')
def users_views():
    return "这是users中的首页"
