__author__ = "Peter"

# 类方法    只能访问类变量，不能访问实例变量
# 在Python中使用比较少，类方法传入的第一个参数为cls，是类本身
class Dog(object):
    n = 333
    def __init__(self, name):
        self.name = name
        self.n  = 353

    @classmethod
    def eat(self):
        print("%s 可以访问类变量 " % (self.n))
        print("%s 不可以访问实例变量 %s" % (self.name))

    def talk(self):
        print("%s is talking" % self.name)


d = Dog("ChenRonghua")
d.eat()
