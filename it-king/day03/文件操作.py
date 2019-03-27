# Author: Peter
# http://www.cnblogs.com/alex3714/articles/5717620.html
# data = open("yesterday", encoding="utf-8").read()
# print(data)

# f = open("yesterday2", 'a', encoding="utf-8")
# f.write('\ntest')
# f.write('\ntest')
# f.close()


# 不建议这种操作，文件很大的时候占内存
# f = open("yesterday", "r", encoding="utf-8")
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print('----------')
#         continue
#     print(line.strip())


#  建议的写法
# count = 0
# f = open("yesterday", "r", encoding="utf-8")
# for line in f:
#     if count == 9:
#         print('---------------')
#         count += 1
#         continue
#     print(line.strip())
#     count += 1
# f.close()


# tell seek
# f = open("yesterday", "r", encoding="utf-8")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
# print(f.encoding)
# print(dir(f.buffer))
# print(f.fileno())
# f.flush()
# f.close()

# f = open("yesterday2", "r+", encoding="utf-8")
# # f = open("yesterday2", "w+", encoding="utf-8")       # 写读，先写新建一个文件，覆盖，然后读
# # f = open("yesterday2", "a+", encoding="utf-8")       # 追加读写
# # f = open("yesterday2", "rb")       # 二进制读
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.write('------------tsss-------')
# print(f.readline())

f = open("yesterday2", 'wb')  # 二进制写
f.write("hello binary\n".encode())
f.close()
