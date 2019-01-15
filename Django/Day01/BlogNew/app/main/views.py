# 处理main业务中的路由和视图处理函数
import os

from . import main
from .. import db
from ..models import *
from flask import render_template, request, session, redirect
import datetime


@main.route('/')
def main_index():
    # 查询Category中所有的数据
    categories = Category.query.all()
    # 查询Topic中所有的数据
    topics = Topic.query.all()
    # 从session中获取登录信息(id,loginname)
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('index.html', params=locals())


@main.route('/login', methods=['GET', 'POST'])
def login_views():
    if request.method == 'GET':
        # 判断id和loginname是否在session中
        if 'id' in session and 'loginname' in session:
            return redirect('/')
        # 记录请求的源地址,并将请求源地址保存进session
        url = request.headers.get('Referer', '/')
        session['url'] = url
        return render_template('login.html')
    else:
        # 接收传递过来的用户名或密码
        loginname = request.form['username']
        upwd = request.form['password']
        # 验证用户名和密码是否正确
        user = User.query.filter_by(loginname=loginname, upwd=upwd).first()
        # 如果登录成功,存进session,则返回到请求的源地址
        if user:
            session['id'] = user.ID
            session['loginname'] = loginname
            url = session['url']
            return redirect(url)
        else:
            # 如果失败,则返回到登录页面
            return render_template('login.html')


@main.route('/logout')
def logout_views():
    # 获取请求源地址,如果没有则将/作为请求源地址
    url = request.headers.get('Referer', '/')
    # 判断session中是否有登录信息,如果有则清除
    if 'id' in session and 'loginname' in session:
        del session['id']
        del session['loginname']
    # 重定向到请求源地址上
    return redirect(url)


@main.route('/release', methods=['GET', 'POST'])
def realease_views():
    if request.method == 'GET':
        # 判断是否有登录用户
        if 'id' in session and 'loginname' in session:
            # 有登录用户，则取出信息判断is_author
            user = User.query.filter_by(ID=session['id']).first()
            # 判断is_author
            if user.is_author:
                # 读取category所有信息
                categories = Category.query.all()
                return render_template('release.html', params=locals())
        # 从哪来回哪去
        url = request.headers.get('Referer', '/')
        return redirect(url)
    else:
        # post请求处理发表博客的相关操作
        # 1.创建Topic的对象-topic
        topic = Topic()
        # 2.接收前端传递过来的值并赋值给topic
        # 2.1 接收传递过来的标题title - author
        topic.title = request.form['author']
        # 2.2 接收传递过来的blogtype_id - list
        topic.blogtype_id = request.form['list']
        # 2.3 接收传递过来的category_id - category
        topic.category_id = request.form['category']
        # 2.4 从session中得到用户的user_id - session['id']
        topic.user_id = session['id']
        # 2.5 接收传递过来的content - content
        topic.content = request.form['content']
        # 2.6 获取系统时间(年月日时分秒)给pub_date
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("标题:%s,类型:%s,内容类型:%s,用户:%s,内容:%s,时间:%s" % (
        topic.title, topic.blogtype_id, topic.category_id, topic.user_id, topic.content, topic.pub_date))
        # 3.判断是否有文件上传,如果有的话则将保存至static/upload,并将路径给images
        if request.files:
            # 获取要上传的文件
            f = request.files['picture']
            # 处理文件名:时间.扩展名
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = f.filename.split('.')[1]
            filename = ftime + '.' + ext
            # 处理上传路径: static/upload
            topic.images = "upload/" + filename
            # 将文件以文件名的形式保存到指定路径下
            basedir = os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir, 'static/upload', filename)
            f.save(upload_path)
        # 4.将topic保存回数据库
        db.session.add(topic)
        return redirect('/')


@main.route('/info')
def info_views():
    # 1.接收传递过来的id参数值(即想查看的博客的id)
    topic_id = request.args['id']
    # 2.根据id查询出对应的博客
    topic = Topic.query.filter_by(id=topic_id).first()
    # 3.更新阅读量(将原有的read_num+1再存进去)
    topic.read_num = int(topic.read_num) + 1
    db.session.add(topic)
    db.session.commit()
    # 4.查询上一篇(查询出id比当前topic_id小的博客中的最后一篇博客,如果结果为None则表示没有上一篇了)
    prevTop = db.session.query(Topic).filter(Topic.id < topic_id).order_by('id desc').first()
    # 5.查询下一篇(查询出id比当前topic_id大的博客中的第一篇博客,如果结果为None则表示没有下一篇了)
    nextTop = db.session.query(Topic).filter(Topic.id > topic_id).first()
    pass
