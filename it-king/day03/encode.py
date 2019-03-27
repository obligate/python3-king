# -*- coding:utf-8 -*-
__author__ = "Peter"

import sys
print(sys.getdefaultencoding())

s = "你哈"
s_gbk = s.encode("gbk")

print(s_gbk)
print(s.encode())   # 默认是文件的编码utf-8

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("utf8", gbk_to_utf8)
