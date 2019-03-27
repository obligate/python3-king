# Author: Peter
# 通过gevent实现单线程下的多socket并发
# 先运行当前程序
# 后运行06_6_1socket_client.py
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)  # 把新的request交给一个新的线程


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(9999)
