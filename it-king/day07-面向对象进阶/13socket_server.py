__author__ = "Peter"

# -*-coding:utf-8-*-
# 服务器端,先启动
# 1次只能和一个client，会话，其他进来的会话挂起，等上个会话结束

import socket
# import os
server = socket.socket()
server.bind(('localhost', 6969))  # 绑定本地要监听的端口
server.listen(5)  # 监听，最大挂起的连接个数为5    backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5,这个值不能无限大，因为要在内核中维护连接队列

print("我要开始等电话了")
while True:
    conn, addr = server.accept()  # 等电话打进来
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    print("电话来了")
    count = 0
    while True:  # 接听电话，开始聊天
        data = conn.recv(1024)
        print("recv:", data.decode())
        if not data:   # 如果客户端断开了，退出，继续等待电话进来
            print("client has lost...")
            break
        # res = os.popen(data).read()  # 发送命令,client不能使用top,可以发送top -bn 1
        # conn.send(res)
        conn.send(data.upper())
        count += 1
        if count > 10:   # 防止进行死循环（linux &mac），可以加一个循环次数控制
          break

server.close()
