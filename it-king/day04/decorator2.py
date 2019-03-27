__author__ = "Peter"
# + 高阶函数
#   + 把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
#   + 返回值中包含函数名


# import time
# def bar():
#     time.sleep(3)
#     print('in the bar')
#
# def test1(func):
#     start_time=time.time()
#     func()    #run bar
#     stop_time=time.time()
#     print("the func run time is %s" %(stop_time-start_time))
#
# test1(bar)
# bar()


# x=1
# y=x
#
# func=bar
# func()



import time


def bar():
    time.sleep(3)
    print('in the bar')


def test2(func):
    print(func)
    return func


# print(test2(bar))
bar = test2(bar)
bar()  # run bar
