# Author: Peter


import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n, sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):  # 定义每个线程执行的函数
        print("running task ", self.n)
        time.sleep(self.sleep_time)
        print("task done,", self.n)


t1 = MyThread("t1", 2)
t2 = MyThread("t2", 4)

t1.start()  # 启动线程t1
t2.start()  # 启动线程t2

t1.join()  # 等待t1线程执行完毕
t2.join()  # 等待t2线程执行完毕

print("main thread....")
