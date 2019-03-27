__author__ = "Peter"

from lib.aa import C

obj = C()
print(obj.__module__)  # 输出 lib.aa，即：输出模块, 表示当前操作的对象C在哪个模块
print(obj.__class__)  # 输出 lib.aa.C，即：输出类， 表示当前操作的对象的类是什么，就是类本身
