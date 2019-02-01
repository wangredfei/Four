import urllib.request

# 定义常用变量
url = 'http://www.baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
# 1.创建请求对象
req = urllib.request.Request(url,
                       headers=headers)
# 2.获取响应对象
res = urllib.request.urlopen(req)
# 3.获取响应内容
html = res.read().decode('utf-8')

# 响应对象的方法
# 获取HTTP的响应码
print(res.getcode())
# 获取返回实际数据的URL
print(res.geturl())











