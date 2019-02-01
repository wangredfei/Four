import requests

# 测试网址,能显示出口IP
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
# 普通代理
#proxies = {'http':'http://113.122.168.131:9999'}
# 私密代理
proxies = {'http':'http://309435365:szayclhp@106.12.214.83:16816'}

res = requests.get(url,
                   proxies=proxies,
                   headers=headers,
                   timeout=3)
res.encoding = 'utf-8'
print(res.text)











