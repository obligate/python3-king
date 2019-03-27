# Author: Peter
import copy
content = ['a', 'b', 'c', 'd']
print(content)
print(content[1:3])
#  从左往右遍历，-2代表倒数第二个开始
print(content[-2])
print(content[-3:-1])  #代表从倒数第三个开始，到倒数第一个结束，不包含尾部[)
print(content[-2:])  # 代表从倒数第二个开始，到最后
content.append("e")
del content[0]
print(len(content))


person = ['name', ['saving', 100]]

'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''
p1 = person[:]  # 完全切片，浅copy
p2 = person[:]

p1[0]='alex'
p2[0]='fengjie'

p1[1][1]=50

print(p1)
print(p2)