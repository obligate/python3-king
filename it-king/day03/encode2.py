# -*-coding:gbk-*-
__author__ = "Peter"

import sys

print(sys.getdefaultencoding())

s = "你哈"  # 在Python3中默认就是unicode编码，转成bytes数组
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))  # 需要把文件的编码变成gbk才可以，否则会报错
