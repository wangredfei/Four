# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from So.items import SoItem
import json


class SoSpider(scrapy.Spider):
    name = "so"
    allowed_domains = ["image.so.com"]
    # start_urls = ['http://image.so.com/']
    #重写Spider中的start_requests()方法,自己指定起始URL地址
    def start_requests(self):
        #想办法拼接URL地址,并发给调度器
        baseurl = 'http://image.so.com/zj?'
        for page in range(2):
            params = {
                'ch': 'beauty',
                'sn': str(page*30),
                'listtype': 'new',
                'temp': '1'
            }
            params = urllib.parse.urlencode(params)
            url = baseurl + params
            yield scrapy.Request(url,callback=self.parseImage)

    def parseImage(self, response):
        item = SoItem()
        #获取响应内容
        html = response.text
        imgDict = json.loads(html)

        for img in imgDict['list']:
            item['imgLink'] = img['qhimg_url']
            yield item
