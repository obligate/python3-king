# Author: Peter

# 生产者消费者模型
# 在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度

import threading
import time
import queue

q = queue.Queue(maxsize=10)


def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头", count)
        count += 1
        time.sleep(0.1)     # 调整生产者的生产数据的速度


def Consumer(name):
    # while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." % (name, q.get()))
        time.sleep(1)     # 调整消费者的消费数据的速度


p = threading.Thread(target=Producer, args=("Alex",))
c = threading.Thread(target=Consumer, args=("ChengRonghua",))
c1 = threading.Thread(target=Consumer, args=("王森",))

p.start()
c.start()
c1.start()
