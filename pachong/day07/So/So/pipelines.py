# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#导入定义好的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

#继承scrapy的图片管道类
class SoPipeline(ImagesPipeline):
    #重写方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['imgLink'])
