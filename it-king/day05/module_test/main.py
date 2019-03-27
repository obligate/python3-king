__author__ = "Peter"

import sys, os

print(sys.path)

x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)

# import module_peter
# module_peter=all_code     module_peter.name           module_peter.logger()


# from module_peter import *    # 不建议使用，此时把module_peter的信息都导入到当前的类中，容易造成冲突

# from module_peter import name # 只把module_peter中的name导入到当前的代码中，直接执行就可以

import module_peter

module_peter.say_hello()
