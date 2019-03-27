from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # 对象名称必须是register，不能修改


# a. app下创建templatetags目录
# b. 任意xxoo.py文件
# c. 创建template对象 register
# d.
#     @register.simple_tag
#     def func(a1,a2,a3....)
#         return "asdfasd"
# e. settings中注册APP
# f. 顶部 {% load xxoo %}
# g. {% 函数名 arg1 arg2 %}
#
# simple_tag: 任意传递参数，但是不能用作布尔判断
# 在tpl4.html中调用
# {% houyafan 2 5 6 %}
@register.simple_tag
def houyafan(a1, a2, a3):
    return a1 + a2


# a. app下创建templatetags目录
# b. 任意xxoo.py文件
# c. 创建template对象 register
# d.
#     @register.filter
#     def func(a1,a2)
#         return "asdfasd"
# e. settings中注册APP
# f. 顶部 {% load xxoo %}
# g. {{ 参数1|函数名:"参数二，参数三" }} {{ 参数1|函数名:数字 }}
#
# filter: 最多只能传递二个参数，可以用作布尔判断
# 在tpl4.html中调用
# {{ "maliya"|jiajingze:30 }}
@register.filter
def jiajingze(a1, a2):
    print(a2, type(a2))
    return a1 + str(a2)
