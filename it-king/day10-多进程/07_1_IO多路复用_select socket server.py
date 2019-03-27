# Author: Peter

import select
import socket
import queue

server = socket.socket()
server.bind(('localhost', 9000))
server.listen(1000)

server.setblocking(False)  # 不阻塞,没有链接就会报错

msg_dic = {}

inputs = [server, ]
# inputs = [server,conn] #[conn,]
# inputs = [server,conn,conn2] #[conn2,]
outputs = []  #
# outputs = [r1,] #
while True:
    # select.select()
    # 参数1，让Kernel监测100个链接，有活跃的把这100个返回
    # 参数2, 返回给用户的链接，需要把哪些数据返回给用户，把对应的链接加上即可
    # 参数3，让kernael监测100个链接，有异常的把这个100个返回
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)
    for r in readable:
        if r is server:  # 代表来了一个新连接
            conn, addr = server.accept()
            print("来了个新连接", addr)
            inputs.append(conn)  # 是因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错了，
            # 所以要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn
            msg_dic[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据
        else:  # conn2
            data = r.recv(1024)
            print("收到数据", data)
            msg_dic[r].put(data)

            outputs.append(r)  # 放入返回的连接队列里
            # r.send(data)
            # print("send done....")

    for w in writeable:  # 要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)  # 返回给客户端源数据

        outputs.remove(w)  # 确保下次循环的时候writeable,不返回这个已经处理完的连接了

    for e in exceptional:   # 如果客户端lost了，server不需要进行监测了，直接在inputs、outputs和队列中remove就可以了
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)

        del msg_dic[e]
