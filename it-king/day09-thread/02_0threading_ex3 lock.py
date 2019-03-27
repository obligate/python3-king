# Author: Peter

# 线程锁(互斥锁Mutex)
# 一个进程下可以启动多个线程，多个线程共享父进程的内存空间，也就意味着每个线程可以访问同一份数据，此时，如果2个线程同时要修改同一份数据，会出现什么状况？
import threading
import time


def run(n):
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    lock.release()


lock = threading.Lock()
num = 0
t_objs = []  # 存线程实例
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_objs.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs:  # 循环线程实例列表，等待所有线程执行完毕
    t.join()

print("----------all threads has finished...", threading.current_thread(), threading.active_count())

print("num:", num)
