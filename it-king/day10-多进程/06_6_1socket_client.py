# Author: Peter
# 通过gevent实现单线程下的多socket并发
# 先运行06_6_0协程gevent_socket_server.py
# 后运行当前程序
import socket

HOST = 'localhost'      # The remote host
PORT = 9999             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)

    #
    print('Received', data)
s.close()
