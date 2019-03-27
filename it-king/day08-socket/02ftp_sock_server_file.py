# Author: Peter
import socket
import os
import hashlib

# ftp server，先启动服务端,启动客户端，执行get  xx文件名
# 本地生成一个大文件： sudo dd if=/dev/sda1 of=test.dd
# 1.读取文件名
# 2.检测文件是否存在
# 3.打开文件
# 4.检测文件大小
# 5.发送文件大小给客户端
# 6.等客户端确认
# 7.开始边读边发数据
# 8.发送md5

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
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename, "rb")
            m = hashlib.md5()       # 创建一个md5对象
            file_size = os.stat(filename).st_size   # 获取文件大小
            conn.send(str(file_size).encode("utf-8"))
            conn.recv(1024)      # wait for ack,防止粘包
            for line in f:
                # m.update(line)   # 更新md5的值
                conn.send(line)  # 边读边发
            # print("file md5", m.hexdigest())   # 获取文件的md5值
            f.close()
            # conn.send(m.hexdigest().encode())  # 发送md5到客户端
        print("send done!!!")
server.close()
