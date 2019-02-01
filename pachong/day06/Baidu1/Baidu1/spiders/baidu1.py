# -*- coding: utf-8 -*-
import scrapy


class Baidu1Spider(scrapy.Spider):
    # 爬虫名
    name = "baidu1"
    # 允许要爬取的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('*' * 50)
        with open('百度.html','w',encoding="utf-8") as f:
            f.write(response.text)
        print('*' * 50)
