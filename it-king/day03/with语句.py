__author__ = "Peter"

# with语句，为了避免打开文件后忘记关闭，可以通过with管理上下文
# with open('log','r') as f:
# ...
# 如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。
# 在Python2.7后，with又支持同时对多个文件的上下文进行管理。

# f = open("yesterday2","r",encoding="utf-8")

with open("yesterday2", "r", encoding="utf-8") as f, \
        open("yesterday2", "r", encoding="utf-8") as f2:
    for line in f:
        print(line.strip())
