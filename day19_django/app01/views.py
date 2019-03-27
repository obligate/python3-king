from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # obj = models.UserInfo.objects.filter(username=u, password=p).first()
        # print(obj)# obj None,
        # count = models.UserInfo.objects.filter(username=u, password=p).count()
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')
    else:
        return redirect('/index/')


from app01 import models


def orm(request):
    # 创建
    # models.UserInfo.objects.create(username='root', password='123')
    #
    # dic = {'username': 'eric', 'password': '666'}
    # models.UserInfo.objects.create(**dic)
    #
    # obj = models.UserInfo(username='alex', password='123')
    # obj.save()

    # 查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root', password='123')
    #
    # # result,QuerySet => Django => []
    # # [obj(id,username,password),obj(id,username,password), obj(id,username,password)]
    # for row in result:
    #     print(row.id, row.username, row.password)
    # print(result)

    # 删除
    # models.UserInfo.objects.filter(username="alex").delete()

    # 更新
    # models.UserInfo.objects.filter(id=3).update(password="69")

    # 一对多
    # user_list = models.UserInfo.objects.all()

    # 两种方式都可以
    # 第一种
    # models.UserInfo.objects.create(
    #     username='root1',
    #     password='123',
    #     email="asdfasdf",
    #     test="asdfasdf",
    #     user_group = models.UserGroup.objects.filter(id=1).first()
    # )
    # 第二种，建议这种
    models.UserInfo.objects.create(
        username='alex',
        password='123',
        email="asdfasdf",
        test="asdfasdf",
        user_group_id=1
    )

    # models.UserGroup.objects.create(
    #     caption='Dev'
    # )
    return HttpResponse('orm')


def index(request):
    return render(request, 'index.html')


def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html', {'user_list': user_list, "group_list": group_list})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        ugi = request.POST.get('group_id')
        models.UserInfo.objects.create(username=u, password=p, user_group_id=ugi)
        return redirect('/cmdb/user_info/')
        # user_list = models.UserInfo.objects.all()
        # return render(request, 'user_info.html', {'user_list': user_list})


def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # 去单挑数据，如果不存在，直接报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})


def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')


def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p)
        return redirect('/cmdb/user_info/')
