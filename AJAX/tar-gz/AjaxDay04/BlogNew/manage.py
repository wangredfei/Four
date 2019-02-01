#启动和项目管理的相关操作代码
#通过Manager()管理项目,并增加数据迁移指令
from app import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
#导入所有的实体类方便使用db指令管理
from app.models import *

app = create_app()
#创建Manager对象用于托管app
manager = Manager(app)
#创建Migrate对象用于关联要管理的app和db
migrate = Migrate(app,db)
#再通过Manager对象增加db迁移指令并指定指令集
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()
