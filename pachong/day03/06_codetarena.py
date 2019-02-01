import requests
import re 

class NoteSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        # 定义Web客户端验证
        self.auth = ('tarenacode','code_2013')
        
    def getParsePage(self):
        # 获取页面
        res = requests.get(url=self.url,
                    auth=self.auth,
                    headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        # 解析页面
        p = re.compile('<a href="(.*?)/.*?</a>',re.S)
        rList = p.findall(html)
        self.writePage(rList)
        # ['AIDCode','']
    
    def writePage(self,rList):
        with open('Note.txt','a') as f: 
            for rs in rList:
                if rs != '..':
                    f.write(rs + '\n')
        print('写入成功')

if __name__ == '__main__':
    spider = NoteSpider()
    spider.getParsePage()










