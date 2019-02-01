import requests
import pymongo
from bs4 import BeautifulSoup

class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.conn = pymongo.MongoClient(
                        '172.40.91.200',27017)
        self.db = self.conn['lianjiadb']
        self.myset = self.db['houseinfo']

    # 获取页面
    def getPage(self):
        res = requests.get(self.url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)

    # 解析并保存数据
    def parsePage(self,html):
        soup = BeautifulSoup(html,'lxml')
        # 找到每个房源的节点对象列表
        rList = soup.find_all('li',
            attrs={'class':'clear LOGCLICKDATA'})
        for r in rList:
            #####################################
            # 找houseInfo节点
            houseInfo = r.find('div',attrs={'class':'houseInfo'})
            infoList = houseInfo.get_text().split('/')
            # 德露苑 /2室1厅/71.4平米/南/简装/无电梯
            name = infoList[0].strip()
            huxing = infoList[1].strip()
            area = infoList[2].strip()
            ##############################################
            # positionInfo信息
            positionInfo = r.find('div',
                    attrs={'class': 'positionInfo'})
            pList = positionInfo.get_text().split('/')
            # print(pList)
            # ['低楼层(共18层)', '2000年建塔楼', '五棵松']
            floor = pList[0]
            year = pList[1]
            address = pList[2]
            #########################################
            # 单价 和 总价
            totalPrice = r.find('div',
                {'class':'totalPrice'}).get_text()
            unitPrice = r.find('div',
                {'class':'unitPrice'}).get_text()
            ########################################
            d = {
                '名称' : name,
                '户型' : huxing,
                '面积' : area,
                '楼层' : floor,
                '年份' : year,
                '地点' : address,
                '总价' : totalPrice,
                '单价' : unitPrice
            }
            self.myset.insert_one(d)

    # 主函数
    def workOn(self):
        self.getPage()

if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.workOn()