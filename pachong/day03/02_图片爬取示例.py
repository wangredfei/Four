import requests

# 常用变量
url = 'https://b-ssl.duitang.com/uploads/item/201511/24/20151124202100_iynLH.jpeg'
headers = {'User-Agent':'Mozilla/5.0'}
# 发请求
res = requests.get(url,headers=headers)
# 获取bytes响应内容
html = res.content
# 保存到本地 ：颖宝.jpg
with open('颖宝.jpg','wb') as f:
    f.write(html)

print('图片下载成功')









