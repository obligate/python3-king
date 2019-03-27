__author__ = "Peter"


# 属性方法  把一个方法变成一个静态属性
class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property  # 定义一个属性
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter  # 添加属性的set方法
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

    def talk(self):
        print("%s is talking" % self.name)

    def __call__(self, *args, **kwargs):
        print("running call", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name


#  调用属性方法
# d = Dog("ChenRonghua")
# d.eat = "包子"  # 赋值
# d.eat          # 调用
# del d.eat      # 删除私有属性 __food
# d.eat          # 报错


# 类的特殊成员方法
print(Dog.__doc__)   # 表示类的描述信息
print(Dog.__dict__)   # 打印类里的所有属性，不包括实例属性
d = Dog("ChenRonghua")
print(d.__dict__)     # 打印所有实例属性，不包括类属性
print(d)             # __str__

