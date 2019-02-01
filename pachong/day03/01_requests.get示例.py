import requests

# 定义常用变量
url = 'http://www.baidu.com/'
headers = {'User-Agent':'Mozilla/5.0'}
# 发请求,获取响应对象
res = requests.get(url,headers=headers)
# 响应对象的属性
# encoding : 响应内容的编码
res.encoding = 'utf-8'
# text : 获取响应内容,字符串
html = res.text
# content : 获取内容,bytes
print(type(res.content))
# status_code : HTTP响应码
print(res.status_code)
# url : 返回实际数据的URL地址
print(res.url)















