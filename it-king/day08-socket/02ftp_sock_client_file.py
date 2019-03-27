# Author: Peter
import socket

client = socket.socket()
client.connect(("localhost", 9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)             # 获取服务端发送过来的文件大小
        print("servr response:", server_response)
        client.send(b"ready to recv file")               # 发送一个ack到服务端
        file_total_size = int(server_response.decode())  # 文件大小
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new", "wb")                # 下载服务端返回的文件，到当前位置
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            f.write(data)                                # 边收边写， 边收文件，边写到指定的位置
            # print(file_total_size,received_size)
        else:
            print("file recv done", received_size, file_total_size)
            f.close()

client.close()
