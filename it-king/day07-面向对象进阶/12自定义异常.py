# Author: Peter
class MyException(Exception):
    def __init__(self, msg):
        self.message = msg


try:
    raise MyException('数据库连不上')
except MyException as e:
    print(e)
