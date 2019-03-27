# 知识点：
## URL
- 两个
## Views
```
- 请求的其他信息
from django.core.handlers.wsgi import WSGIRequest
request.environ
request.environ['HTTP_USER_AGENT']
```

## Templates
- 母版...html
    + extends
    + include
- 自定义函数 tpl4.html
```
因为在模板语言中不能够做运算等一些稍显复杂的操作，所以在Django中提供了两种自定制标签，一种是simple_tag，一种是filter
```
    + simple_tag
    ```
    a. app下创建templatetags目录
    b. 任意xxoo.py文件
    c. 创建template对象 register
    d. 
        @register.simple_tag
        def func(a1,a2,a3....)
            return "asdfasd"
    e. settings中注册APP
    f. 顶部 {% load xxoo %}
    g. {% 函数名 arg1 arg2 %}
    缺点：
        不能作为if条件
    优点：
        参数任意
    ```
			
	+ filter
	```
	a. app下创建templatetags目录
    b. 任意xxoo.py文件
    c. 创建template对象 register
    d. 
        @register.filter
        def func(a1,a2)
            return "asdfasd"
    e. settings中注册APP
    f. 顶部 {% load xxoo %}
    g. {{ 参数1|函数名:"参数二，参数三" }} {{ 参数1|函数名:数字 }}
    缺点：
        最多两个参数，不能加空格
    优点：
        能作为if条件
	```
		
## 分页（自定义的分页）
+ XSS：
	+ 模板中使用 `{{ page_str|safe }}`
	+ 后端封装输出 `mark_safe(page_str)`	
	
## Cookie
客户端浏览器上的一个文件 ,以键值对存储的{"user": 'dachengzi'}

+ 1、获取Cookie：
```
request.COOKIES['key']
request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
    参数：
        default: 默认值
           salt: 加密盐
        max_age: 后台控制过期时间
```
+ 2、设置Cookie：
```
rep = HttpResponse(...) 或 rep ＝ render(request, ...)
rep.set_cookie(key,value,...)
rep.set_signed_cookie(key,value,salt='加密盐',...)
    参数：
        key,              键
        value='',         值
        max_age=None,     超时时间
        expires=None,     超时时间(IE requires expires, so set it if hasn't been already.)
        path='/',         Cookie生效的路径，/ 表示根路径，特殊的：跟路径的cookie可以被任何url的页面访问
        domain=None,      Cookie生效的域名
        secure=False,     https传输
        httponly=False    只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
```
+ 3. 由于cookie保存在客户端的电脑上，所以，JavaScript和jquery也可以操作cookie。
```
<script src='/static/js/jquery.cookie.js'></script>
$.cookie("list_pager_num", 30,{ path: '/' });
```

## 装饰器
```
FBV:
def auth(func):
    def inner(reqeust,*args,**kwargs):
        v = reqeust.COOKIES.get('username111')
        if not v:
            return redirect('/login/')
        return func(reqeust, *args,**kwargs)
    return inner

CBV:
from django import views
from django.utils.decorators import method_decorator

@method_decorator(auth,name='dispatch')
class Order(views.View):

# @method_decorator(auth)
# def dispatch(self, request, *args, **kwargs):
#     return super(Order,self).dispatch(request, *args, **kwargs)

# @method_decorator(auth)
def get(self,reqeust):
    v = reqeust.COOKIES.get('username111')
    return render(reqeust,'index.html',{'current_user': v})

def post(self,reqeust):
    v = reqeust.COOKIES.get('username111')
    return render(reqeust,'index.html',{'current_user': v})
```