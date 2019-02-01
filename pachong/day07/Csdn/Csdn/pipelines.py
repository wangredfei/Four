# -*- coding: utf-8 -*-

import pymongo
import pymysql
from Csdn.settings import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnPipeline(object):
    def process_item(self, item, spider):
        print('------------------------------')
        print(item['title'])
        print(item['time'])
        print(item['number'])
        print('------------------------------')
        return item

class CsdnMongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        self.db =self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self,item,spider):
        #把item转换为字典
        d = dict(item)
        self.myset.insert_one(d)
        return item

class CsdnMysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into csdntab values(%s,%s,%s)'
        L = [item['title'],item['time'],item['number']]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()