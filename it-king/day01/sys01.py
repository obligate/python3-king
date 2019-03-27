# Author: Peter

import sys
import os

# print(sys.path)
print(sys.argv)
# cmd_res = os.system('dir')  # 执行命令，不保存结果,此时cmd_res仅仅返回命令执行的结果
cmd_res = os.popen('dir').read()
print('--->', cmd_res)

# os.mkdir('newdir')
