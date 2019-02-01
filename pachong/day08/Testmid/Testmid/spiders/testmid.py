# -*- coding: utf-8 -*-
import scrapy


class TestmidSpider(scrapy.Spider):
    name = 'testmid'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('这是parse函数的输出!')