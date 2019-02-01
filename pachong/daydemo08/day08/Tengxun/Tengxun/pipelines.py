# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TengxunPipeline(object):
    def process_item(self, item, spider):
        print('*********************')
        print(item['zhName'])
        print(item['zhType'])
        print(item['zhNum'])
        print(item['zhAddress'])
        print(item['zhTime'])
        print(item['zhLink'])
        print('*********************')
        return item

import pymongo
from Tengxun.settings import *

class TengxunMongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST,
                                        MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self,item,spider):
        d = dict(item)
        self.myset.insert_one(d)
        return item

    def close_spider(self,spider):
        print('执行close_spider函数,结束!!!')



