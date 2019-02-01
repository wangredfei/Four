# 导入selenium中webdriver接口
from selenium import webdriver
import time

# 创建phantomjs浏览器对象
driver = webdriver.Chrome()
# 用get方法发请求
driver.get('http://www.baidu.com/')
# 获取响应内容
print(driver.page_source)
# 获取屏幕截图
driver.save_screenshot('百度.png')
# 关闭浏览器
time.sleep(5)
driver.quit()





