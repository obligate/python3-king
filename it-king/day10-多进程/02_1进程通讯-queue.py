# Author: Peter

# 不同进程间内存是不共享的，要想实现两个进程间的数据交换
# Queues 进程间数据传递
# 使用方法跟threading里的queue差不多
from multiprocessing import Process, Queue


def f(qq):
    print("in child:", qq.qsize())
    qq.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    q.put("test123")
    p = Process(target=f, args=(q,))  # 把queue传进入到子进程，此时是copy了一份，两个进程的q不是一个q，是两个不同的q，之间通过一个中间方进行传递
    p.start()
    p.join()
    print("444", q.get_nowait())
    print("444", q.get_nowait())

# 线程是数据共享
# import threading
# import queue
#
#
# def f():
#     q.put([42, None, 'hello'])
#
#
# if __name__ == '__main__':
#     q = queue.Queue()
#     p = threading.Thread(target=f)
#     p.start()
#     p.join()
#     print("444", q.get())
