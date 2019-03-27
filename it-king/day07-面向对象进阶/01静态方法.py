__author__ = "Peter"

import os


# os.system()
# os.mkdir()

class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod  # 实际上跟类没什么关系了，只是名义上归类管, 实际上在静态方法里访问不了类或实例中的任何属性,如果想要用self的属性，可以传入self
    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))

    @staticmethod
    def eatNoSelf():
        print("eat static method no self ")

    def talk(self):
        print("%s is talking" % self.name)


# 实例调用
d = Dog("ChenRonghua")
d.eat(d)  # 不能调用类中的属性和方法，也可以在方法中传入self的实例的D
d.talk()

# 类名称调用
Dog.eatNoSelf()
