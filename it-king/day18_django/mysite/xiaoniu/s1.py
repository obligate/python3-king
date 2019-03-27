# Author: Peter
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("我是小牛")
