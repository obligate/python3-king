# Author: Peter
# 1. 启动代码
# 2. 浏览器访问： http://127.0.0.1:8000/

# 上述通过socket来实现了其本质，而对于真实开发中的python web程序来说，一般会分为两部分：服务器程序和应用程序。
# 服务器程序负责对socket服务器进行封装，并在请求到来时，对请求的各种数据进行整理。应用程序则负责具体的逻辑处理。
# 为了方便应用程序的开发，就出现了众多的Web框架，例如：Django、Flask、web.py 等。
# 不同的框架有不同的开发方式，但是无论如何，开发出的应用程序都要和服务器程序配合，才能为用户提供服务。
# 这样，服务器程序就需要为不同的框架提供不同的支持。这样混乱的局面无论对于服务器还是框架，都是不好的。
# 对服务器来说，需要支持各种不同框架，对框架来说，只有支持它的服务器才能被开发出的应用使用。这时候，标准化就变得尤为重要。
# 我们可以设立一个标准，只要服务器程序支持这个标准，框架也支持这个标准，那么他们就可以配合使用。
# 一旦标准确定，双方各自实现。这样，服务器可以支持更多支持标准的框架，框架也可以使用更多支持标准的服务器。
import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf-8"))
    client.send("Hello, Seven".encode("utf-8"))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()


