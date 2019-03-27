__author__ = "Peter"
# 客户端
import socket

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 9999))  # 连接本地的6969端口

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:   # client不能发送空，否则server一直挂起，所以需要加一个判断，如果为空，不允许发送
        continue
    client.send(msg.encode("utf-8"))
    data = client.recv(10240)
    print("recv:", data.decode())
    # print(data.decode())   # 接受命令的返回结果

client.close()

