#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from flask import Flask, request, render_template
import datetime

app = Flask(__name__)


@app.route('/01-file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        # #测试时间问题
        # print(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
        return render_template('01-file.html')
    else:
        uname = request.form.get('uname')
        print('用户名:' + uname)

        # 获取文件：uimg
        f = request.files['uimg']
        # 保存路径：static/upload/时间.jpg

        # 获取当前时间
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

        # 获取当前文件的扩展名
        ext = f.filename.split('.')[1]

        # 组合成新的文件名
        filename = ftime + '.' + ext
        print('文件名称为：' + filename)

        # 获取绝对路径
        basedir = os.path.dirname(__file__)

        # 完整路径=绝对路径+保存目录+文件名称
        upload_path = os.path.join(basedir, 'static/upload', filename)
        print('上传路径：' + upload_path)
        f.save(upload_path)
        return '获取文件成功'


if __name__ == '__main__':
    app.run(debug=True)
