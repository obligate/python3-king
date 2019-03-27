# Author: Peter
# 1. 时间戳   time.time()
# 2. 格式化字符串
# 3. 元组(struct_time)共九个元素 time.localtime()
import time

print(time.time())  # 1970年1月1号开始到现在的秒数
print(time.localtime())
print(time.gmtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))  # 将utc struct_time格式转成指定的字符串格式

# %a    本地（locale）简化星期名称
# %A    本地完整星期名称
# %b    本地简化月份名称
# %B    本地完整月份名称
# %c    本地相应的日期和时间表示
# %d    一个月中的第几天（01 - 31）
# %H    一天中的第几个小时（24小时制，00 - 23）
# %I    第几个小时（12小时制，01 - 12）
# %j    一年中的第几天（001 - 366）
# %m    月份（01 - 12）
# %M    分钟数（00 - 59）
# %p    本地am或者pm的相应符    一
# %S    秒（01 - 61）    二
# %U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。    三
# %w    一个星期中的第几天（0 - 6，0是星期天）    三
# %W    和%U基本相同，不同的是%W以星期一为一个星期的开始。
# %x    本地相应日期
# %X    本地相应时间
# %y    去掉世纪的年份（00 - 99）
# %Y    完整的年份
# %Z    时区的名字（如果不存在为空字符）
# %%    ‘%’字符


import datetime

print(datetime.datetime.now())  # 返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  # 时间替换
