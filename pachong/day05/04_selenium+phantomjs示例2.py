from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.PhantomJS()
# 打开百度
driver.get('http://www.baidu.com/')
print(driver.page_source.find('ldjfdjlflsadldkfjdl'))


# # 接收终端输入内容发送到搜索框
# key = input('请输入要搜索的内容:')
# driver.find_element_by_id('kw').send_keys(key)
# # 点击：百度一下
# su = driver.find_element_by_id('su')
# su.click()
# time.sleep(1)
# # 屏幕截图
# driver.save_screenshot('result.png')
# # 关闭浏览器
# driver.quit()









