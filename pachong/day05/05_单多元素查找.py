# 导入webdriver接口
from selenium import webdriver

# 创建浏览器对象
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(options=opt)
# 向百科发请求 https://www.qiushibaike.com/text/
driver.get('https://www.qiushibaike.com/text/')
# 查找 class 为 content 的第1个节点，并获取文本内容
content = driver.find_element_by_class_name('content')
print(content.text)
print('*' * 40)
# 查找class 为 content 的所有节点，并获取每个节点文本内容
contents = driver.find_elements_by_class_name('content')
for c in contents:
    print(c.text)
    print('='*40)