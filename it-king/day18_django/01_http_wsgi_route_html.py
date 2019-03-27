# Author: Peter
from wsgiref.simple_server import make_server


def index():
    f = open('html/index.html', mode='rb')
    data = f.read()
    print(data)
    print([data])
    return [data, ]


def login():
    f = open('html/login.html', mode='rb')
    data = f.read()
    return [data, ]


def routers():
    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
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
