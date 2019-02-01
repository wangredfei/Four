import urllib.request

# 向网站发请求获取响应对象
url = 'http://www.baidu.com/'
res = urllib.request.urlopen(url)
# 获取响应对象的内容
print(res.read().decode('utf-8'))

# res.read() 得到类型为：bytes
# decode('utf-8') 得到类型: string

# encode() : 字符串->bytes
# decode() : bytes->字符串









