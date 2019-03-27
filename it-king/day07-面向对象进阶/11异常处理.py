__author__ = "Peter"

# 演示错误
names = ['peter', 'jack']
# names['sdfsdf']      # IndexError

data = {}
# data['name']         # KeyError

# 捕获异常
try:
    open("tes.txt")          #   主代码块
    # data['name']
    # names[3]
except (KeyError, IndexError) as e:  # 异常时，执行该块
    print("没有这个key", e)
except IndexError as e:
    print("列表操作错误", e)
except BaseException as e:
    print("未知错误", e)
else:
    print("一切正常")    # 主代码块执行完，执行该块
finally:                # 无论异常与否，最终执行该块
    print("不管有没有错，都执行")
