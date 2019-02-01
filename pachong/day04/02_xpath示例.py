from lxml import etree

html = '''<div class="wrapper">
	<i class="iconfont icon-back" id="back"></i>
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
	</ul>
	<i class="iconfont icon-liebiao" id="menu"></i>
</div>'''
# 创建解析对象
parseHtml = etree.HTML(html)
# 调用xpath返回结束,text()为文本内容
rList = parseHtml.xpath('//a/text()')
#print(rList)

# 提取所有的href的属性值
r2 = parseHtml.xpath('//a/@href')
#print(r2)

# 提取所有href的值,不包括 / 
r3 = parseHtml.xpath(
    '//ul[@id="nav"]/li/a/@href')
#print(r3)
# 获取 图片、军事、...,不包括新浪社会
r4 = parseHtml.xpath(
    '//ul[@id="nav"]/li/a/text()')
for r in r4:
    print(r)











