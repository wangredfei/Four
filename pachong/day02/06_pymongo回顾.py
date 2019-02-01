import pymongo

DBNAME = 'spiderdb'
TABNAME = 't1'

# 创建连接对象
conn = pymongo.MongoClient('192.168.56.131',27017)
# 创建库对象
db = conn[DBNAME]
# 创建集合对象
myset = db[TABNAME]
# 插入文档
myset.insert_one({"name":"Lucy"})

#mongo
#show dbs
#use spiderdb
#show collections
#db.t1.find().pretty()
#db.dropDatabase()















