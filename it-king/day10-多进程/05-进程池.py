# Author: Peter
# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
# 进程池中有两个方法：
# apply
# apply_async
from multiprocessing import Process, Pool, freeze_support
import time
import os


def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


###################################################
# 1.串行，一个一个的输出
# if __name__ == '__main__':
#     # freeze_support()  # 只在windows需要
#     pool = Pool(processes=3)  # 允许进程池同时放入3个进程
#     print("主进程", os.getpid())
#     for i in range(10):
#         pool.apply(func=Foo, args=(i,))  # 串行
#     print('end')
#     pool.close()

#####################################################
# # 2.并行,3个3个的输出，记住必须加上join
# # pool.join() 进程池中执行完毕后再关闭，如果注释，那么程序直接关闭。.join()
# if __name__ == '__main__':
#     # freeze_support()  # 只在windows需要
#     pool = Pool(processes=3)  # 允许进程池同时放入3个进程
#     print("主进程", os.getpid())
#     for i in range(10):
#         pool.apply_async(func=Foo, args=(i,))  # 并行
#     print('end')
#     pool.close()
#     pool.join()  # 进程池中执行完毕后再关闭，如果注释，那么程序直接关闭。.join()

#########################################################
# 3.并行，支持回调，同时3个输出，每3个3个的输出
# 是主进程调用的回调
if __name__ == '__main__':
    pool = Pool(processes=3)  # 允许进程池同时放入5个进程
    print("主进程", os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback=回调，是在父进程进行回调
    print('end')
    pool.close()
    pool.join()  # 进程池中执行完毕后再关闭，如果注释，那么程序直接关闭。.join()
