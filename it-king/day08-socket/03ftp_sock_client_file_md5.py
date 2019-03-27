# Author: Peter
import socket
import hashlib

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
        m = hashlib.md5()                                # 生成md5校验对象
        while received_size < file_total_size:
            # 解决粘包的问题
            # 主要是最后一次的包有可能出现粘包的情况，只判断最后一次还剩多少，只收剩下的部分
            if file_total_size - received_size > 1024:  # 要收不止一次，只收1024即可
                size = 1024
            else:  # 最后一次了，剩多少收多少
                size = file_total_size - received_size
                print("last receive:", size)
            data = client.recv(size)

            received_size += len(data)
            m.update(data)
            f.write(data)                                # 边收边写， 边收文件，边写到指定的位置
            # print(file_total_size,received_size)
        else:
            new_file_md5 = m.hexdigest()                 # 获取收取文件的md5码
            print("file recv done", received_size, file_total_size)
            f.close()
        # 进行md校验
        server_file_md5 = client.recv(1024)
        print("server file md5:", server_file_md5.decode("utf-8"))
        print("client file md5:", new_file_md5)

client.close()
