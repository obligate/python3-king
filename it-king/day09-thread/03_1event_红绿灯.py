# Author: Peter

import time
import threading

# 通过Event来实现两个或多个线程间的交互
# 下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则。
# event
# An event is a simple synchronization object
# the event represents an internal flag, and threads
# can wait for the flag to be set, or set or clear the flag themselves.
# event = threading.Event()
# a client thread can wait for the flag to be set
# event.wait()
# a server thread can set or reset it
# event.set()      If the flag is set, the wait method doesn’t do anything.
# event.clear()    If the flag is cleared, wait will block until it becomes set again
# Any number of threads may wait for the same event.
event = threading.Event()


# 红绿灯
# 循环设置标志位
def lighter():
    count = 0
    event.set()  # 先设置绿灯，刚开始设置为绿灯，否则<5的时候状态不明确
    while True:
        if count > 5 and count < 10:  # 改成红灯
            event.clear()  # 把标志位清了
            print("\033[41;1mred light is on....\033[0m")
        elif count > 10: # 此时红灯变成绿灯，红灯持续时间为5秒
            event.set()  # 变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on....\033[0m")
        time.sleep(1)
        count += 1

# 车
# 循环检测标志位
def car(name):
    while True:
        if event.is_set():  # 代表绿灯
            print("[%s] running..." % name)
            time.sleep(1)
        else:
            print("[%s] sees red light , waiting...." % name)
            event.wait()   # a client thread can wait for the flag to be set
            print("\033[34;1m[%s] green light is on, start going...\033[0m" % name)


light = threading.Thread(target=lighter, )
light.start()

car1 = threading.Thread(target=car, args=("Tesla",))
car1.start()
