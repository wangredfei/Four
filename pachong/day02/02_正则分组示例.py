import re 

s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))

# 先按照整体正则匹配出来,然后再匹配()中
# 如果有2个(),则以元组形式显示









