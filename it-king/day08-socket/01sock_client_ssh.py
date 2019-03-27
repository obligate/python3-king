# Author: Peter
import socket

client = socket.socket()
client.connect(("localhost", 9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)  # 接受命令结果的长度,此时返回的结果是bytes类型，需要int(cmd_res_size.decode("utf-8")) 转成int
    print("命令结果大小：", cmd_res_size)
    client.send("准备好接受了，可以准备发了".encode("utf-8")) # 防止服务端发送的数据粘包，客户端给发一个ack的消息
    # 根据长度，循环接受数据
    reveived_size = 0
    received_data = b''
    while reveived_size != int(cmd_res_size.decode("utf-8")):
        data = client.recv(1024)
        reveived_size += len(data)  # 每次收到的有可能小于1024，所以必须用len判断
        received_data += data
        # print(data.decode("utf-8"))
    # cmd_res = client.recv(1024)
    # print(cmd_res.decode("utf-8"))
    else:
        print("cmd res receive done!!!", reveived_size)
        print(received_data.decode("utf-8"))

client.close()
