from bs4 import BeautifulSoup

html = '''<div class="test">雄霸</div>'''
# 创建解析对象
soup = BeautifulSoup(html,'lxml')
# 调用find_all方法,返回列表
rList = soup.find_all('div',attrs={'class':'test'})
for r in rList:
    print(r.get_text())






