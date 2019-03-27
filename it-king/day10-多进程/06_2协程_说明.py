# Author: Peter

# 遇到IO就会切换
# home出现sleep，切换到执行bbs，bbs出现sleep，就会切换到login，什么时候切回去呢？
# IO切换完毕就切回去，如何实现的呢？
import time


def home():
    print("in func 1")
    time.sleep(5)               # get data from db
    print("home exec done ")


def bbs():
    print("in func 2")
    time.sleep(2)


def login():
    print("in func 3")
