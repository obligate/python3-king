# Author: Peter
# __call__ 对象后面加括号，触发执行
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()


class Foo:

    def __init__(self):
        print('_init__')

    def __call__(self, *args, **kwargs):
        print('__call__', args, kwargs)


obj = Foo()  # 执行 __init__
obj(1, 2, 3, name=33)  # 执行 __call__
