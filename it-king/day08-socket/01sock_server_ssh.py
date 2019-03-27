# Author: Peter
import socket
import os
import time

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(5)
while True:
    conn, addr = server.accept()  # 开始阻塞，等待
    print("new conn", addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令：", data)
        cmd_res = os.popen(data.decode("utf-8")).read()  # 接受字符串，执行结果也是字符串
        print("before send ", len(cmd_res))
        # 不能发空数据，如果为null，可以自己造一个数据过去
        if len(cmd_res) == 0:
            cmd_res = "cmd has not output"
        # cmd_res.encode("utf-8") 会有中文的字符长度问题，一个中文3个字节，必须用encode()
        conn.send(str(len(cmd_res.encode("utf-8"))).encode("utf-8"))   # 先把返回的文件大小发送给客户端
        # 防止粘包
        # 1. 客户端发一个ack响应   client.send("准备好接受了，可以准备发了".encode("utf-8"))
        # 2. 服务端接受ack    client_ack = conn.recv(1024)
        # time.sleep(0.5)    # 防止粘包 第一种方法
        client_ack = conn.recv(1024)    # wait client to confirm,防止粘包 第二种方法，等待客户端输入信息，客户端加一个send给服务端一个响应
        print("ack from client:", client_ack.decode("utf-8"))
        conn.send(cmd_res.encode("utf-8"))  # 发送数据
        print("send done!!!")
server.close()
