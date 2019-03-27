__author__ = "Peter"


# 创建对象的两个方式
# 1. 普通方式
# obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，Foo类本身也是一个对象，因为在Python中一切事物都是对象。
# 如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，那么Foo类对象应该也是通过执行某个类的 构造方法 创建
# 所以，f对象是Foo类的一个实例，Foo类对象是 type 类的一个实例，即：Foo类对象 是通过type类的构造方法创建
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
# obj = Foo("peter")
# print(type(obj))    # 输出：<class '__main__.Foo'>     表示，obj 对象由Foo类创建
# print(type(Foo))     # 输出：<type 'type'>              表示，Foo类对象由 type 类创建


# 2. 特殊方式
def func(self):
    print('hello %s' % self.name)


def __init__(self, name, age):
    self.name = name
    self.age = age


# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员
Foo = type('Foo', (object,), {'talk': func, '__init__': __init__})
print(type(Foo))
f = Foo("Chrn", 22)
f.talk()

