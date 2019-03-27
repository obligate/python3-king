__author__ = "Peter"

# 嵌套函数
# 返回值
def foo():
    print('in the foo')

    def bar():
        print('in the bar')

    bar()


foo()
