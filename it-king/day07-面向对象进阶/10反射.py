__author__ = "Peter"


# 反射
#     hasattr(obj,name_str) , 判断一个对象obj里是否有对应的name_str字符串的方法
#     getattr(obj,name_str),  根据字符串去获取obj对象里的对应的方法的内存地址
#     setattr(x,'y',z),       is equivalent to ``x.y = v''
#     delattr                 删除属性

def bulk(self):
    print("%s is yelling...." % self.name)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating..." % self.name, food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d, choice):
    # delattr(d,choice)
    func = getattr(d, choice)
    # func("骨头")  要是属性会报错
else:  # 动态装配方法bulk
    setattr(d, choice, bulk)  # d.talk = bulk
    func = getattr(d, choice)
    func(d)

# print(d.name)   删除打印会报错
