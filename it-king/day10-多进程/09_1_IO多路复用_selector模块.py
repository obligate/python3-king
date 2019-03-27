# Author: Peter
# 默认使用epoll，如果系统不支持，就使用select，例如windows只支持select
import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr, mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 新连接注册read回调函数


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else: # 没有收到数据，说明链接断了，需要移除服务端的监听的链接
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()   # 默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data  # accept
        callback(key.fileobj, mask)  # key.fileobj=  文件句柄
