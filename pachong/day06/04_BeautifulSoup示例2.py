from bs4 import BeautifulSoup

html = '''<div class="test1">雄霸</div>
<div class="test1">幽若</div>
<div class="test2">
    <span>第二梦</span>
</div>'''
# class为test1的div的文本内容
soup = BeautifulSoup(html,'lxml')
rList = soup.find_all('div',{'class':'test1'})
for r in rList:
    # print(r.get_text())
    pass

rList = soup.find_all('div',{'class':'test2'})
for r in rList:
    # print(r.get_text())
    print(r.span.string)



