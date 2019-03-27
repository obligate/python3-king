__author__ = "Peter"


# 用于索引操作，如字典。进行获取、设置、删除数据
# 可以把一个实例做成一个字典

class Foo(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()
obj['name'] = "peter"      # 设置 自动触发执行 __setitem__
ret = obj['name']         # 获取 自动触发执行 __getitem__
print(ret)
del obj["sdfdsf"]          # 删除 自动触发执行 __delitem__

print(obj.data)

