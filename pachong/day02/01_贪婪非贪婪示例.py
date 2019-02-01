import re 

html = '''
<div><p>仰天大笑出门去</p></div>
<div><p>我辈岂是蓬蒿人</p></div>
'''
# 贪婪匹配 .*
p = re.compile('<div><p>.*</p></div>',re.S)
rList = p.findall(html)
#print(rList)

# 非贪婪匹配 : .*?
p = re.compile('<div><p>.*?</p></div>',re.S)
rList = p.findall(html)
print(rList)









