# Author: Peter
# 1. 启动程序
# 2. 浏览器访问： http://127.0.0.1:8000/
# WSGI（Web Server Gateway Interface）是一种规范，它定义了使用python编写的web app与web server之间接口格式，实现web app与web server间的解耦。
# python标准库提供的独立WSGI服务器称为wsgiref。
from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    # environ 客户端发来的所有数据
    # start_response 封装要返回给用户的数据，响应头的状态
    # python3 string --> byte
    # 1.  b'fff'
    # 2. 'ff'.encode('utf-8')
    # 3. bytes('ff',encoding='utf-8')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
