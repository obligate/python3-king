# Author: Peter

import threading
import time

# Daemon守护线程，主线程不会等待守护线程执行完毕，主线程只会等守护线程
# 当主线程退出，守护线程也会结束
# 守护线程(slave) 服务与非守护线程(master)，守护线程服务于非守护线程，类似主仆关系，如果非守护线程挂了，守护线程也就挂了
def run(n):
    print("task ", n)
    time.sleep(2)
    print("task done", n, threading.current_thread())


start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程，必须在start之前设置
    t.start()

# time.sleep(2)  主线程也sleep 2s
print("----------all threads has finished...", threading.current_thread(), threading.active_count())
print("cost:", time.time() - start_time)
