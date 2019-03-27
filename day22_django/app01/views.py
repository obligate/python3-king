from django.shortcuts import render, redirect, HttpResponse


# Create your views here.


def login(request):
    # 了解django.conf 中的setting，比setting.py大得多
    #  程序启动的时候先加载setting.py的内容到内存，然后赋值给setting，修改其默认值
    # from django.conf import settings
    # print(settings.CSRF_HEADER_NAME)
    # HTTP_X_CSRFTOKEN
    # X-CSRFtoken

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == "123":
            # session中设置值
            # 表示django处理的事情有
            # 1. 生成随机字符串
            # 2. 写到用户浏览器cookie
            # 3. 保存到session中,session在django中默认在sqlite3中django_session表中
            # 4. 在随机字符串对应的字典中设置相关内容。。
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('rmb', None) == '1':
                # 设置超时时间
                request.session.set_expiry(10)  # 保存10s，10s后session就会失效，不设置，默认是2周内有效
            return redirect('/index/')
        else:
            return render(request, 'login.html')


# django为用户实现防止跨站请求伪造的功能，通过中间件 django.middleware.csrf.CsrfViewMiddleware 来完成。而对于django中设置防跨站请求伪造功能有分为全局和局部。
# 全局：
# 　　中间件 django.middleware.csrf.CsrfViewMiddleware
# 局部：
# @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。
# @csrf_exempt， 取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
# 注：from django.views.decorators.csrf import csrf_exempt,csrf_protect

from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_protect
def index(request):
    # session中获取值
    # 1.获取当前用户的随机字符串
    # 2.根据随机字符串获取对应的信息，在对应的信息里面就有is_login的信息
    if request.session.get('is_login', None):  # request.session['is_login'] 如果is_login没有会报错
        return render(request, 'index.html', {'username': request.session['username']})
    else:
        return HttpResponse('gun')


def logout(request):
    # del request.session['username']
    request.session.clear()
    return redirect('/login/')


###################### 中间件 ###########################
class Foo:
    def __init__(self, req, html, dic):
        self.req = req
        self.html = html
        self.dic = dic

    def render(self):
        # // 创建钩子
        return render(self.req, self.html, self.dic)


def test(request, nid):
    # int('ddddddssss')   # 测试中间件的异常情况
    print('小姨妈-->没带钱')

    # return HttpResponse('ok')
    # return render(request, 'index.html', {...})   # 此时中间件的process_template_response才会执行
    return Foo(request, 'index.html', {'k1': 'v1'})  # 定义一个class，必须有render方法，process_template_response才会执行


###################  cache # #######################
# 优先级
# 全站缓存 > views cache > html cache
# 用django的生命周期就可以解释
# 1. 当请求到中间件的时候，有满足条件的cache，就直接返回了
# 2. 如果到达中间件还没有cache，就会使用views cache
# 3. 如果到达views还没有cache，就会使用html cache
####
# 1. 全站缓存，使用中间件进行处理，不用自己写，直接配置就可以
# 使用中间件，经过一系列的认证等操作，如果内容在缓存中存在，则使用FetchFromCacheMiddleware获取内容并返回给用户，当返回给用户之前，判断缓存中是否已经存在，如果不存在则UpdateCacheMiddleware会将缓存保存至缓存，从而实现全站缓存
#     MIDDLEWARE = [
#         'django.middleware.cache.UpdateCacheMiddleware',
#         # 其他中间件...
#         'django.middleware.cache.FetchFromCacheMiddleware',
#     ]
# 2. views cache配置
# 2.1 视图函数添加@cache_page(10)
# 2.2 html中直接使用即可 {{ ctime }}
#
# 3. html cache配置，范围比views cache小，只对html标签做缓存,
# 3.1 html页头添加{% load cache %}
# 3.2 需要缓存的地方添加
# {% cache 10 c1 %}
#     <h1>{{ ctime }}</h1>
# {% endcache %}
from django.views.decorators.cache import cache_page


# @cache_page(10)
def cache(request):
    import time
    ctime = time.time()
    return render(request, 'cache.html', {'ctime': ctime})


# 1. 内置信号
# 由于内置信号的触发者已经集成到Django中，所以其会自动调用，而对于自定义信号则需要开发者在任意位置触发。
# + 定义内置信号的回调函数sg.py
# + 在day22_django的__init__.py进行导入import sg
# 2. 自定义信号
# a. 定义信号
# b. 注册信号
# c. 触发信号
def signal(request):
    from app01 import models

    obj = models.UserInf(user='root')
    print('end')
    obj.save()

    obj = models.UserInf(user='root')
    obj.save()

    obj = models.UserInf(user='root')
    obj.save()

    # 自定义信号
    # 	- 自定义
    # 		 - 定义信号
    # 		 - 出发信号
    # 		 - 信号中注册函数
    # 定义信号第一步，第二步，在sg.py定义即可
    # 1. 定义信号
    # import django.dispatch
    # pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])
    #
    # # 2. 注册信号
    # def callback(sender, **kwargs):
    #     print("callback")
    #     print(sender, kwargs)
    #
    # pizza_done.connect(callback)
    # 在views中触发信号
    from sg import pizza_done
    pizza_done.send(sender="asdfasdf", toppings=123, size=456)  # sender是谁发送的，随便传，后面的参数，是我们定义信号的参数
    return HttpResponse('ok')


######################## Form #####################
from django import forms
from django.forms import widgets
from django.forms import fields


class FM(forms.Form):
    # 字段本身只做验证
    user = fields.CharField(   # 对应的是<input name="user" />
        error_messages={'required': '用户名不能为空.'},
        widget=widgets.Textarea(attrs={'class': 'c1'}),
        label="用户名",
        # initial='root',
    )
    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6', "max_length": '密码长度不能大于12'},
        widget=widgets.PasswordInput(attrs={'class': 'c2'})
    )
    email = fields.EmailField(error_messages={'required': '邮箱不能为空.', 'invalid': "邮箱格式错误"})

    f = fields.FileField()

    # p = fields.FilePathField(path='app01')

    city1 = fields.ChoiceField(
        choices=[(0, '上海'), (1, '广州'), (2, '东莞')]
    )
    city2 = fields.MultipleChoiceField(
        choices=[(0, '上海'), (1, '广州'), (2, '东莞')]
    )


from app01 import models
def fm(request):
    if request.method == "GET":
        # 从数据库中吧数据获取到
        dic = {
            "user": 'r1',
            'pwd': '123123',
            'email': 'sdfsd',
            'city1': 1,
            'city2': [1, 2]
        }
        obj = FM(initial=dic)
        return render(request, 'fm.html', {'obj': obj})
    elif request.method == "POST":
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            # obj.cleaned_data
            models.UserInf.objects.create(**obj.cleaned_data)
        else:
            # ErrorDict
            # print(obj.errors.as_json())
            # print(obj.errors['user'][0])
            return render(request, 'fm.html', {'obj': obj})
        return render(request, 'fm.html')
