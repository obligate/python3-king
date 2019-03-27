__author__ = "Peter"


# 类默认是由 type 类实例化产生，type类中如何实现的创建类？类又是如何创建对象？
# 答：类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，所以，我们可以为 __metaclass__ 设置一个type类的派生类，从而查看 类 创建的过程
# 类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__
# MyType不适用于Python3.x,创建过程有所改变
class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call---")

        obj = self.__new__(self, *args, **kwargs)
        obj.data = {"name": 111}
        self.__init__(obj, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs):
        print("Foo --new--")
        # print(object.__new__(cls))
        return object.__new__(cls)  # 继承父亲的__new__方法


# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo("Peter")
print(obj.name)
