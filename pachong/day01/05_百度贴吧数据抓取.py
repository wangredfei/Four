import urllib.request
import urllib.parse
import random
import time 

# 定义常用变量
baseurl = 'http://tieba.baidu.com/f?'
hList = [
            {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
            {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
            {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}    
    ]
headers = random.choice(hList)
# 接收用户从终端输入
name = input('请输入贴吧名称:')
begin = int(input('请输入起始页:'))
end = int(input('请输入终止页:'))
# 拼接贴吧URL
kw = urllib.parse.urlencode({'kw':name}) 
# 拼接每一页的URL地址,发请求
for page in range(begin,end+1):
    pn = (page-1)*50
    url = baseurl+kw+'&pn='+str(pn)
    # 三步走
    req = urllib.request.Request(url,
                     headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存到本地
    filename = '第'+str(page)+'页.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)
        print('第 %d 页爬取成功' % page)
        time.sleep(0.1)















