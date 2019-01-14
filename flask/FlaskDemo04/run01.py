#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
import datetime
import os

app = Flask(__name__)


@app.route('/02-dsc', methods=['POST', 'GET'])
def dsc_viw():
    if request.method == 'GET':
        return render_template('02-dsc.html')
    else:
        uname = request.form.get('uname')
        f = request.files['uimg']
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        ext = f.filename.split('.')[-1]
        filename = ftime + '.' + ext
        basedir = os.path.dirname(__file__)
        upload_w = os.path.join(basedir, 'static/upload', filename)
        f.save(upload_w)
        return '获取文件成功'


if __name__ == '__main__':
    app.run(debug=True)
