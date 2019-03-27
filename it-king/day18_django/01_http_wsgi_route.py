# Author: Peter
# 通过python标准库提供的wsgiref模块开发一个自己的Web框架
from wsgiref.simple_server import make_server


def index():
    return ['index'.encode("utf-8")]


def login():
    return ['login'.encode("utf-8")]


def routers():
    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
    )

    return urlpatterns


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return ['404 not found'.encode("utf-8")]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
