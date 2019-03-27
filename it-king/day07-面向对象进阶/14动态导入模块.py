# Author: Peter

modname = "lib.aa"

# 1. 动态导入模块方法1： __import__
# 说明：
# 　　1. 函数功能用于动态的导入模块，主要用于反射或者延迟加载模块。
# 　　2. __import__(module)相当于import module
# 在lib目录平级新建一个测试的模块，使用 __import__ 动态以字符串形式导入lib下的aa模块

# from lib import aa
# from lib import "aa"  # 不可以，如何实现
lib = __import__(modname)  # 这是解释器自己内部用的
obj = lib.aa.C()
print(obj.name)

# 2. 动态导入模块方法2：import importlib
# 实例还是上面的lib.aa模块，这里使用importlib进行动态导入（这个方法好理解，也是官方建议使用的）
import importlib

aa = importlib.import_module(modname)
obj = aa.C()
print(obj.name)


# 3. 反射
mod = __import__(modname)
print(mod)
instance = getattr(mod.aa, "C")
obj = instance()
print(obj.name)


assert type(obj.name) is str
assert type(obj.name) is int   # 出错就不会往下走



