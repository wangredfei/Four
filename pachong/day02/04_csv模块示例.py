import csv

with open('teacher.csv','w',newline='') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 利用写入对象的writerow方法写入数据
    writer.writerow(['旭哥',37])
    writer.writerow(['超哥',28])