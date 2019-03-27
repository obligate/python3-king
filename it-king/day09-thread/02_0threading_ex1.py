# Author: Peter

import threading
import time


def run(n):
    print("task", n)
    time.sleep(2)
    print("task done", n)


#  多线程并发
t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))
t1.start()
t2.start()

# 调用方式
# run("t1")
# run("t2")


# 循环启动50个线程，主线程和子线程并行，这样统计的时间不是所有的子线程的时间
# start_time = time.time()
# for i in range(50):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
# print("----------all threads has finished...")
# print("cost:", time.time() - start_time)


# join
start_time = time.time()
t_objs = []  # 存线程实例
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()  # 启动线程
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs:  # 循环线程实例列表，等待所有线程执行完毕
    t.join()  # 阻塞线程

print("----------all threads has finished...")
print("cost:", time.time() - start_time)
