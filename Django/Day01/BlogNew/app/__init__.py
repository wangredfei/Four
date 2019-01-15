# 当前程序的初始化操作
# 主要工作
# 1.构建Flask应用实例以及各种配置
# 2.创建SQLAlchemy的应用实例
# 3.关联蓝图(BluePrint)程序
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 声明SQLAlchemy的应用实例
db = SQLAlchemy()


def create_app():
    # 创建Flask程序实例
    app = Flask(__name__)
    # 配置启动模式为调试模式
    app.config['DEBUG'] = True
    # 配置数据库的连库信息
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/blog"
    # 配置数据库的自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 配置session所需要的SECRET_KEY
    app.config['SECRET_KEY'] = 'suinibian'

    # 关联db以及app
    db.init_app(app)

    # 将main蓝图程序与app关联到一起
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # 将user蓝图程序与app关联到一起
    from .users import user as user_blueprint
    app.register_blueprint(user_blueprint)

    # 返回已创建好的Flask程序实例
    return app
