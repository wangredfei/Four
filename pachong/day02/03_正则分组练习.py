import re 

html = '''<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  </p>

  <p class="contents">
    Two tigers two tigers run fast
  </p>
</div>

<div class="animal">
  <p class="name">
    <a title="Rabbit"></a>
  </p>

  <p class="contents">
    Small white rabbit white and white 
  </p>
</div>'''
# 创建编译对象
p = re.compile('<div class="animal".*?title="(.*?)".*?class="contents">(.*?)</p>',re.S)
rList = p.findall(html)
#print(rList)
# 第2步实现
for r in rList:
    print('动物名称:',r[0])
    print('动物描述:',r[1].strip())
    print('*' * 30)

#<div class="animal".*?title="(.*?)"\
#.*?class="contents">(.*?)</p>















