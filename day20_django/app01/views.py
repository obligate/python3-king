from django.shortcuts import render, HttpResponse, redirect
import json
from app01 import models


# Create your views here.


def business(request):
    v1 = models.Business.objects.all()
    # QuerySet
    # [obj(id,caption,code),obj(id,caption,code),obj(id,caption,code) ]
    v2 = models.Business.objects.all().values('id', 'caption')
    # QuerySet
    # [{'id':1,'caption': '运维'},{'id':1,'caption': '开发'},...]
    v3 = models.Business.objects.all().values_list('id', 'caption')
    # QuerySet
    # [(1,'运维'),(2,'开发')]
    return render(request, 'business.html', {'v1': v1, 'v2': v2, 'v3': v3})


# 页面采用模态对话框的形式
def host(request):
    if request.method == 'GET':
        v1 = models.Host.objects.filter(nid__gt=0)
        # for row in v1:
        #     print(row.nid, row.hostname, row.ip, row.port, row.b_id, row.b.id, row.b.caption, row.b.code)
        # return HttpResponse('Host Ok')
        v2 = models.Host.objects.filter(nid__gt=0).values('nid', 'hostname', 'b_id', 'b__caption')
        # for row in v2:
        #     print(row['nid'], row['hostname'], row['b_id'], row['b__caption'])
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'b_id', 'b__caption')

        b_list = models.Business.objects.all()
        return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3, 'b_list': b_list})
    elif request.method == 'POST':
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        # 可以使用b对象也可以使用使用bid
        # 1. 使用b对象，需要查询一次数据库，不建议
        # models.Host.objects.create(hostname=h,
        #                            ip=i,
        #                            port=p,
        #                            b=models.Business.objects.get(id=b)
        #                            )
        # 2. 使用bid
        models.Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b
                                   )
        return redirect('/host')


def test_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 5:
            models.Host.objects.create(hostname=h,
                                       ip=i,
                                       port=p,
                                       b_id=b)
        else:
            ret['status'] = False
            ret['error'] = "太短了"
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))  # dumps 成一个字符串，将dict转换成一个字符串


def test_ajax_update(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        nid = request.POST.get('nid')
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 5:
            models.Host.objects.filter(nid=nid).update(hostname=h,
                                                       ip=i,
                                                       port=p,
                                                       b_id=b)
        else:
            ret['status'] = False
            ret['error'] = "太短了"
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))  # dumps 成一个字符串，将dict转换成一个字符串


def app(request):
    if request.method == "GET":
        app_list = models.Application.objects.all()  # 返回所有的application和host的列表
        # for row in app_list:
        #     print(row.name,row.r.all())
        host_list = models.Host.objects.all()
        return render(request, 'app.html', {"app_list": app_list, 'host_list': host_list})
    elif request.method == "POST":
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        print(app_name, host_list)

        # 1.先在applicatin添加一条数据
        # 2.在第三张表m2m【app01_application_r】中添加host_list数据
        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)
        return redirect('/app')


def ajax_add_app(request):
    ret = {'status': True, 'error': None, 'data': None}

    app_name = request.POST.get('app_name')
    host_list = request.POST.getlist('host_list')
    obj = models.Application.objects.create(name=app_name)
    obj.r.add(*host_list)
    return HttpResponse(json.dumps(ret))
