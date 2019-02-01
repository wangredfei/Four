import pytesseract
# Python图片处理标准库
from PIL import Image

# 创建图片对象
img = Image.open('test1.jpg')
# 图片转字符串
s = pytesseract.image_to_string(img)
print(s)