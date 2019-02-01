import requests

url = 'http://www.baidu.com/s?'
headers = {'User-Agent':'Mozilla/5.0'}
# 接收用户输入内容
key = input('请输入搜索内容:')
# 定义params字典
params = {
        'wd':key,
        'pn':str(10)
    }
# 发请求获取响应对象
# 自动对params字典进行编码,然后和url
# 进行拼接
res = requests.get(url,
                   params=params,
                   headers=headers)
res.encoding = 'utf-8'
# 获取内容 ：文本
html = res.text
print(html)


















