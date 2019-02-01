import requests
from multiprocessing import Queue
from threading import Thread
import json
import time
import urllib.parse

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?'
        self.headers = {'User-Agent':''}
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()

    # URL入队列
    def getUrl(self):
        # 10个URL地址,放到队列中
        for page in range(50):
            params = {
                'page' : str(page),
                'categoryId' : '2',
                'pageSize' : '30'
            }
            # 编码,params:'page=0&categoryId=2&...'
            params = urllib.parse.urlencode(params)
            # 拼接，入队列
            fullurl = self.url + params
            self.urlQueue.put(fullurl)


    # 采集线程事件函数,发请求，把html给解析队列
    def getHtml(self):
        while True:
            # 如果队列不为空,则获取url
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                # 三步走
                res = requests.get(url,
                            headers=self.headers)
                res.encoding = 'utf-8'
                html = res.text
                # 把html放到解析队列
                self.parseQueue.put(html)
            else:
                break

    # 解析线程事件函数,从解析队列get,提取并处理数据
    def parseHtml(self):
        while True:
            if not self.parseQueue.empty():
                # html为json格式的字符串
                html = self.parseQueue.get()
                hList = json.loads(html)['data']
                # hList : [{应用信息1},{},{}]
                for h in hList:
                    # 应用名称
                    name = h['displayName']
                    # 应用链接
                    d = {
                        '应用名称' : name.strip(),
                        '应用链接' : 'http://app.mi.com/details?'\
                                     + h['packageName']
                    }
                    with open('xiaomi.json','a') as f:
                        f.write(str(d) + '\n')
            else:
                break

    # 主函数
    def workOn(self):
        # url入队列
        self.getUrl()
        # 存放所有采集线程对象列表
        t1List = []
        # 存放所有解析线程对象列表
        t2List = []
        # 采集线程开始执行
        for i in range(1):
            t = Thread(target=self.getHtml)
            t1List.append(t)
            t.start()
        # 统一回收采集线程
        for i in t1List:
            i.join()

        # 解析线程开始执行
        for i in range(1):
            t = Thread(target=self.parseHtml)
            t2List.append(t)
            t.start()
        # 统一回收解析线程
        for i in t2List:
            i.join()

if __name__ == '__main__':
    begin = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print('执行时间:%.2f' % (end-begin))






