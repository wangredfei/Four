# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem
from scrapy_redis.spiders import RedisSpider

class TengxunSpider(RedisSpider):
    name = "tengxun"
    allowed_domains = ["hr.tencent.com"]
    url = 'https://hr.tencent.com/position.php?start='
    redis_key = 'tengxunspider:start_urls'

    def parse(self, response):
        for page in range(0,2851,10):
            fullurl = self.url + str(page)
            yield scrapy.Request(fullurl,
                        callback=self.parseHtml)

    def parseHtml(self,response):
        # 创建item对象
        item = TengxunItem()
        # 节点对象列表(基准xpath)
        baseList = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for base in baseList:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()').extract()
            if item['zhType']:
                item['zhType'] = item['zhType'][0]
            else:
                item['zhType'] = '无'
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]

            yield item








