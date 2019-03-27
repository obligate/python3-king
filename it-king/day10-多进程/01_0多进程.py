# Author: Peter
from multiprocessing import Process
import time
import threading


def thread_run():
    print(threading.get_ident())


def f(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_run,)
    t.start()


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=f, args=('bob%s' % i,))
        p.start()
    # p.join()
