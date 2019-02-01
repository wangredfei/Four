def f1():
    print('启动生成器')
    for i in range(2):
        yield i
    print('*' * 30)

g = f1()
while True:
    try:
        print(next(g))
    except:
        break






