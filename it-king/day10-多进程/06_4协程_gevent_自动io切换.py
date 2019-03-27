# Author: Peter
# Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度
import gevent


def foo():
    print('Running in foo')
    gevent.sleep(2)  # 模仿耗时IO
    print('Explicit context switch to foo again')


def bar():
    print('Explicit  context  to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')


def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


gevent.joinall([
    gevent.spawn(foo),  # 生成，
    gevent.spawn(bar),
    gevent.spawn(func3),
])
