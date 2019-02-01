import pymysql 
import warnings

# 连接对象
db = pymysql.connect('localhost','root',
                     '123456',charset='utf8')
# 游标对象
cursor = db.cursor()
# execute()
cdb = 'create database if not exists spider'
udb = 'use spider'
ctab = 'create table if not exists t1(\
        id int)'
ins = 'insert into t1 values(3)'
# 提交到数据库执行
# 过滤警告/忽略警告
warnings.filterwarnings('ignore')

cursor.execute(cdb)
cursor.execute(udb)
cursor.execute(ctab)
cursor.execute(ins)
db.commit()
# 关闭
cursor.close()
db.close()