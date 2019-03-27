# Author: Peter
# 	MVC
# 		Model       View       Controller
# 		数据库       模板文件         业务处理
#
# 	MTV
# 		Model    Template     View
# 		数据库    模板文件      业务处理
from wsgiref.simple_server import make_server
from controller import account


def routers():
    urlpatterns = (
        ('/index/', account.index),
        ('/login/', account.login),
    )

    return urlpatterns


def run_server(environ, start_response):
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
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
