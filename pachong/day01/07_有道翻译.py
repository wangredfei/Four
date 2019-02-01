import urllib.request
import urllib.parse
import json 

# F12或抓包工具抓到的POST的地址
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent':'Mozilla/5.0'}
key = input('请输入要翻译的内容:')
# 处理Form表单数据
data = {
        "i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15481459849821",
        "sign":"a175d6ac9ad751a700fc87f6e738172e",
        "ts":"1548145984982",
        "bv":"363eb5a1de8cfbadd0cd78bd6bd43bee",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false",
    }
data = urllib.parse.urlencode(data).encode('utf-8')
# 三步走
req = urllib.request.Request(url,
                        data=data,
                        headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')

# loads()可把json格式的字符串转为Python
# 的数据类型
rDict = json.loads(html)
result = rDict['translateResult'][0][0]['tgt']
print(result)


#{"type":"ZH_CN2EN",
# "errorCode":0,
# "elapsedTime":0,
# "translateResult":
#   [[{"src":"老虎","tgt":"The tiger"}]]}












