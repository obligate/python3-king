from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


# def index(request):
#     from django.core.handlers.wsgi import WSGIRequest
#     print(type(request))
#     print(request.environ)  # 封装了所有用户请求信息
#     for k, v in request.environ.items():
#         print(k, v)
#     print(request.environ['HTTP_USER_AGENT'])
#     return HttpResponse('Index')


def tpl0(request):
    user_list = [1, 2, 3, 43]
    return render(request, 'tpl0.html', {'u': user_list})


def tpl1(request):
    user_list = [1, 2, 3, 43]
    return render(request, 'tpl1.html', {'u': user_list})


def tpl2(request):
    name = 'root'
    return render(request, 'tpl2.html', {'name': name})


def tpl3(request):
    status = "已经删除"
    return render(request, 'tpl3.html', {'status': status})


def tpl4(request):
    name = "IYMDFjfdf886sdf"
    return render(request, 'tpl4.html', {'name': name})


LIST = []
for i in range(1000):
    LIST.append(i)

# 1. 自己写的分页代码
# def user_list(request):
#     current_page = request.GET.get('p', 1)
#     current_page = int(current_page)
#     per_page_count = 10
#     start = (current_page - 1) * per_page_count
#     end = current_page * per_page_count
#     data = LIST[start:end]
#     all_count = len(LIST)
#     total_count, y = divmod(all_count, per_page_count)
#     if y:
#         total_count += 1
#
#     page_list = []
#     pager_num = 11
#     # start_index = 1
#     # end_index = count + 1
#
#     # start_index = current_page - 5
#     # end_index = current_page + 5 + 1
#
#     if total_count < pager_num:
#         start_index = 1
#         end_index = total_count + 1
#     else:
#         if current_page <= (pager_num + 1) / 2:
#             start_index = 1
#             end_index = pager_num + 1
#         else:
#             start_index = current_page - (pager_num - 1) / 2
#             end_index = current_page + (pager_num + 1) / 2
#             if (current_page + (pager_num - 1) / 2) > total_count:
#                 end_index = total_count + 1
#                 start_index = total_count - pager_num + 1
#     if current_page == 1:
#         prev = '<a  class="page " href="javascript:void(0);">上一页</a>'
#     else:
#         prev = '<a  class="page " href="/user_list/?p=%s">上一页</a>' % (current_page - 1)
#     page_list.append(prev)
#     for i in range(int(start_index), int(end_index)):
#         if i == current_page:
#             temp = '<a  class="page active" href="/user_list/?p=%s">%s</a>' % (i, i)
#         else:
#             temp = '<a  class="page" href="/user_list/?p=%s">%s</a>' % (i, i)
#         page_list.append(temp)
#     if current_page == total_count:
#         next_page = '<a  class="page " href="#">下一页</a>'
#     else:
#         next_page = '<a  class="page " href="/user_list/?p=%s">下一页</a>' % (current_page + 1)
#     page_list.append(next_page)
#
#     jump = """
#         <input  type="text" /><a onclick='jumpTo(this,"/user_list/?p=");' id='ii1'>GO</a>
#         <script>
#             function jumpTo(ths,base){
#                 var val = ths.previousSibling.value;
#                 location.href=base+val
#             }
#         </script>
#     """
#
#     page_list.append(jump)
#     page_str = "".join(page_list)
#     page_str = mark_safe(page_str)
#     return render(request, 'user_list.html', {'li': data, 'page_str': page_str})


# 2. 自己写的分页代码,进行page的封装,封装到uitls/pagination.py
from utils import pagination


def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    # 添加cookie支持
    val = request.COOKIES.get('per_page_count', 10)

    print(val)
    val = int(val)

    page_obj = pagination.Page(current_page, len(LIST), val)
    data = LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('/user_list/')

    return render(request, 'user_list.html', {'li': data, 'page_str': page_str})


########################### cookie ###########################
user_info = {
    'Whisper': {'pwd': "123"},
    'Flash': {'pwd': "123"},
}


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:
            return render(request, 'login.html')
        if dic['pwd'] == p:
            res = redirect('/index/')
            # 1. maxage，N秒后失效
            # res.set_cookie('username', u, max_age=10)
            # 2. expires，什么时候失效即截止时间失效
            # import datetime
            # current_date = datetime.datetime.utcnow()
            # current_date = current_date + datetime.timedelta(seconds=5)
            # res.set_cookie('username', u, expires=current_date)

            res.set_cookie('username', u)  # document.cookie
            res.set_cookie('user_type', "asdfjalskdjf",
                           httponly=True)  # 只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）
            return res
        else:
            return render(request, 'login.html')


# 定义一个auth的装饰器
def auth(func):
    def inner(request, *args, **kwargs):
        v = request.COOKIES.get('username')
        if not v:
            return redirect('/login/')  # 没有登陆，到登陆页面
        return func(request, *args, **kwargs)

    return inner


# FBV的装饰器的使用
@auth
def index(request):
    # 获取当前已经登录的用户
    v = request.COOKIES.get('username')
    # 已经装饰器实现，注释掉
    # if not v:
    #     return redirect('/login/')
    return render(request, 'index.html', {'current_user': v})


# CBV的装饰器使用
from django import views
from django.utils.decorators import method_decorator


@method_decorator(auth, name='dispatch')  # 2. 对所有的方法做用户认证,建议使用
class Order(views.View):

    # @method_decorator(auth) # 1. 对所有的方法做用户认证，也不好，可以把装饰器写在类上 @method_decorator(auth, name='dispatch')
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Order,self).dispatch(request, *args, **kwargs)

    # @method_decorator(auth)   # 3、只对get做用户认证
    def get(self, request):
        v = request.COOKIES.get('username')
        # if not v:
        #     return redirect('/login/')
        return render(request, 'index.html', {'current_user': v})

    # @method_decorator(auth)   # 3.只对post做用户认证
    def post(self, request):
        v = request.COOKIES.get('username')
        return render(request, 'index.html', {'current_user': v})


# def order(request):
#     # 获取当前已经登录的用户
#     v = request.COOKIES.get('username')
#     return render(request, 'index.html', {'current_user': v})


def cookie(request):
    #
    # request.COOKIES
    # request.COOKIES['username']
    request.COOKIES.get('username')

    response = render(request, 'index.html')
    response = redirect('/index/')
    response.set_cookie('key', "value")  # 设置cookie，当关闭浏览器是，cookie失效
    response.set_cookie('username111', "value", max_age=10)  # 设置cookie, N秒后失效
    # 设置cookie, 截止时间失效
    import datetime
    current_date = datetime.datetime.utcnow()
    current_date = current_date + datetime.timedelta(seconds=5)
    response.set_cookie('username111', "value", expires=current_date)
    response.set_cookie('username111', "value", max_age=10)

    # request.COOKIES.get('...')
    # response.set_cookie(...)
    obj = HttpResponse('s')

    # 设置cookie的时候，通过salt加密
    obj.set_signed_cookie('username', "whisper", salt="asdfasdf")
    # 获取cookie的时候，通过salt解密
    request.get_signed_cookie('username', salt="asdfasdf")

    return response
