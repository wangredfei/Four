import urllib.request
import urllib.parse

# 定义常用变量
baseurl = 'http://www.baidu.com/s?wd='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
key = input('请输入要搜索的内容:')
# 对URL编码,拼接URL
key = urllib.parse.quote(key)
url = baseurl + key
print(url)
# 发请求获响应
req = urllib.request.Request(url,
                       headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
# 保存到本地文件 : html是一个字符串
with open('百度.html','w',encoding='gb18030') as f:
    f.write(html)

print('保存成功')












