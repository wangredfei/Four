# -*- coding: utf-8 -*-
import scrapy
#导入items.py中的CsdnItem类
from Csdn.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    #起始URL地址
    start_urls = ['https://blog.csdn.net/cpongo4/article/details/86613730']

    def parse(self, response):
        item = CsdnItem()
        item['title']  = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item['time']   = response.xpath('//span[@class="time"]/text()').extract()[0]
        item['number'] = response.xpath('//span[@class="read-count"]/text()').extract()[0]

        yield  item
