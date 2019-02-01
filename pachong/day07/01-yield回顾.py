#!/usr/bin/env python
# -*- coding:utf-8 -*-
def f1():
    print('启动生成器')
    for i in range(2):
        yield  i
    print('*' * 30)

g = f1()
while True:
    try:
        print(next(g))
    except:
        break
#//h1[@class="title-article"]/text()  //span[@class="time"]/text() //span[@class="read-count"]/text()