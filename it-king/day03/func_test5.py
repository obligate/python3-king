__author__ = "Peter"


def test(x, y, z):
    print(x)
    print(y)
    print(z)


# test(y=2,x=1) #关键字参数调用，与形参顺序无关
# test(1,2)  #位置参数调用，与形参一一对应
# test(x=2,3)
test(3, z=2, y=6)

# 位置参数一定要在关键字后面
