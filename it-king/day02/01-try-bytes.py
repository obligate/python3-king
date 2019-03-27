# Author: Peter
str = "我是中国人"


print(str.encode(encoding="utf-8"))
print(str.encode(encoding="utf-8").decode(encoding="utf-8"))