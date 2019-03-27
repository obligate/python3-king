# Author: Peter

# Without using the lock output from the different processes is liable to get all mixed up.
# windows 不起作用，可以在linux试，了解即可
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()  # windows 不起作用，可以在linux试
    print('hello world', i)
    l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()
