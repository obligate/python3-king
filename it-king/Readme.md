## Refer
+ [知识目录](https://www.cnblogs.com/alex3714/category/770733.html)
+ [知识目录2](http://blog.51cto.com/egon09)
+ [基本语法1](https://www.cnblogs.com/alex3714/articles/5465198.html)
+ [基本语法2-编码](http://www.cnblogs.com/alex3714/articles/5717620.html)
+ [编码](http://www.cnblogs.com/luotianshuai/articles/5735051.html)
+ [基本语法3](http://www.cnblogs.com/alex3714/articles/5740985.html)
+ [mysql](https://www.cnblogs.com/alex3714/articles/5885096.html)


## 函数参数
+ 1.位置参数
+ 2.关键字参数，必须在位置参数后面
+ 3.默认参数，就是给形参直接赋值了一个值
+ 4.参数组
    + `*args`  接受N个位置参数，转换成元组形式
    + `**args` 接受N个关键字参数，转换成字典的方式
    + 命名关键字参数
        + 如果要限制关键字参数的名字，就可以用命名关键字参数
        + 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
        ```python
            def person(name, age, *, city, job):
                print(name, age, city, job)
        ```
        + 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
> 参数定义的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数和关键字参数。
## 局部变量
+ 局部变量只在当前函数生效，例如：字符串，数字类型不可以修改
+ 如果要在函数中修改全局变量，必须用global 声明一下,不要这么使用
```python
school = "Oldboy edu."
def change_name(name):
     global school
     school = "Mage Linux"
     print("before change",name,school)
     name ="Alex li" #这个函数就是这个变量的作用域
     age =23
     print("after change",name)
print("school:",school)
```

## 装饰器
+ 定义： 本质是函数，（装饰其他函数）就是为其他函数添加附加功能
+ 原则：装饰器对被装饰的函数是完全透明的，也就是说被装饰的函数，不知道装饰器的存在
    + 1.不能修改被装饰函数的源代码
    + 2.不能修改被装饰函数的调用方式
+ 只是储备
    + 函数即变量
    + 高阶函数
        + 把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
        + 返回值中包含函数名（不修改函数的调用方式）
    + 嵌套函数

## 模块 & 包
+ 1.定义
    + 模块：用来从逻辑上组织python代码(变量,函数,类,逻辑),本质就是.py结尾的python文件,文件名test.py,模块名test
    + 包：  用来从逻辑上组织模块，本质就是一个目录（必须带有一个__init__.py文件）
+ 2.导入方法
    + import module_name
    + import module_name_1,module_name_2
    + from module_name import *            导入模块中的所有信息，不建议使用
    + from module_name import m1,m2,m3
    + from module_name import m1 as m 
+ 3.import本质（路径搜索和搜索路径）
    + 导入模块的本质就是把python文件解释一遍,就是解释python文件
        + （import test            => test='test.py all code')
        +  (from test import name  => name='code')
    + 导入包的本质就是执行该包下面的__init__.py文件
    + import module_name 就是找到module_name.py，然后解释该python文件--->查找路径在sys.path中定义
+ 4.导入优化
    + from module_name import test
+ 5.模块的分类
    + 标准库（内置模块）
        + `time ` 与 `datetime`
    + 开源模块（第三方模块）
    + 自定义模块
 
 ## class
 + 类
    + python2
        + 经典类   深度优先
        + 新式类   广度优先
    + python3
        + 经典类  广度优先
        + 新式类  广度优先
 + 属性
    + 类属性  `大家共用的属性 ,节省开销`
    + 实例属性
    + 私有属性`__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs`
 + 方法
    + 实例方法 `类方法必须包含参数 self,且为第一个参数`
    + 私有方法`__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods`
    + 构造方法
    + 析构方法
    + 属性方法 `把一个方法变成一个静态属性 @property`
    + 类方法  ` 只能访问类变量，不能访问实例变量`
    `在Python中使用比较少，类方法传入的第一个参数为cls，是类本身。并且，类方法可以通过类直接调用，或通过实例直接调用。但无论哪种调用方式，最左侧传入的参数一定是类本身`
    ```python
    @classmethod
    def func_a(cls):
        print(type(cls), cls)
     if __name__ == '__main__':
        ClassA.func_a()
        ca = ClassA()
        ca.func_a()
    ```
    + 静态方法 `实际上跟类没什么关系了,只是名义上归类管理， 实际上在静态方法里访问不了类或实例中的任何属性`
    ```python
           # 使用@staticmethod装饰器来声明,如果一个类的方法不需要self参数,只能通过类去调用这个方法，如果使用实例调用这个方法会引发异常。
           class ClassA(object):
                @staticmethod
                def func_a():
                    print('Hello Python')
        if __name__ == '__main__':
            ClassA.func_a()
            # 也可以使用实例调用,但是不会将实例作为参数传入静态方法
            ca = ClassA()
            ca.func_a()
    ```
> Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Runoob:
    __site = "www.runoob.com"
runoob = Runoob()
print runoob._Runoob__site
```
## 颜色格式
+ ` echo "\033[字背景颜色;字体颜色m输入的内容\033[0m"`
+ `echo "\033[41;36m write something here \033[0m" ，其中41的位置代表底色, 36的位置是代表字的颜色 `
+ `a1=input("\033[41;36m write something here \033[0m") #前景色和背景色均设置`
+ `a1=input("\033[41;1m write something here \033[0m")#只设置背景色，且加粗`
+ `a1=input("\033[36;1m write something here \033[0m")#可以单独识别只设置字体颜色，且加粗`
+ `a1=input("\033[36;m write something here \033[0m")#可以单独识别只设置字体颜色，不加粗`
+ 字背景颜色范围:40----49 
```
40:黑 
41:深红 
42:绿 
43:黄色 
44:蓝色 
45:紫色 
46:深绿 
47:白色 
```
+ 字颜色:30-----------39 
```
30:黑 
31:红 
32:绿 
33:黄 
34:蓝色 
35:紫色 
36:深绿 
37:白色 
```
+ ANSI控制码的说明
```
\33[0m 关闭所有属性 
\33[1m 设置高亮度 
\33[4m 下划线 
\33[5m 闪烁 
\33[7m 反显 
\33[8m 消隐 
\33[30m -- \33[37m 设置前景色 
\33[40m -- \33[47m 设置背景色 
\33[nA 光标上移n行 
\33[nB 光标下移n行 
\33[nC 光标右移n行 
\33[nD 光标左移n行 
\33[y;xH设置光标位置 
\33[2J 清屏 
\33[K 清除从光标到行尾的内容 
\33[s 保存光标位置 
\33[u 恢复光标位置 
\33[?25l 隐藏光标 
\33[?25h 显示光标  
```

## 线程 & 进程
io 操作不占用cpu，计算占用cpu，python多线程 不适合cpu密集操作型的任务，适合io操作密集型的任务
+ 进程，资源的集合，好比是屋子，至少包含一个线程，不能自己动起来，需要线程去处理
+ 线程，是操作系统最小的调度单位， 是一串指令的集合
    + 线程 内存共享
    + 线程同时修改同一份数据时必须加锁，mutex互斥锁
    + join等待线程执行完毕
    + 递归锁Rlock，锁中有锁
    + 守护线程(slave) 服务与非守护线程(master)，守护线程服务于非守护线程，类似主仆关系，如果非守护线程挂了，守护线程也就挂了
    + queue 解耦，使程序直接实现松耦合， 提高处理效率
## 书籍
+ 追风筝的人
+ 白鹿原
+ 林达看美国
+ 百年孤独
+ 消费者行为学
+ 失控 kk
+ 必然 
+ 浪潮之巅
+ 数学之美