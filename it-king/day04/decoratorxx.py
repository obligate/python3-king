# Author: Peter

import time


def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time %s" % (stop_time - start_time))

    return deco


@timer
def test1():
    print("in the test1")


# test1 = timer(test1)
test1()
