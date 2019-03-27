__author__ = "Peter"

# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
import shelve
import datetime

# 读
d = shelve.open('test_file/shelve_test')  # 打开一个文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
d.close()


# 写
# d = shelve.open('test_file/shelve_test')
# info = {'age': 22, "job": 'it'}
#
# name = ["alex", "rain", "test"]
# d["name"] = name  # 持久化列表
# d["info"] = info  # 持久dict
# d['date'] = datetime.datetime.now()
# d.close()
