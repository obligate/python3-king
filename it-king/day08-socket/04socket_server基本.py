# Author: Peter
import socketserver


# 1. 你必须自己创建一个请求处理类，并且这个类要继承BaseRequestHandler,并且还有重写父亲类里的handle()
# 2. 你必须实例化TCPServer ，并且传递server ip 和 你上面创建的请求处理类 给这个TCPServer
# server.handle_request() #只处理一个请求
# server.serve_forever() #处理多个一个请求，永远执行
# 3. Finally, call server_close() to close the socket.

# 每一个请求过来都会实例化 MyTCPHandler
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))  # 打印客户端的ip地址
                print(self.data)
                if not self.data:  # 客户端断了
                    print(self.client_address, "断开了")
                    break  # 关闭连接
                self.request.send(self.data.upper())  # 把数据返回给客户端
            except ConnectionResetError as e:
                print("err", e)
                break


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    # 支持多并发使用ThreadingTCPServer,默认TCPServer不支持多并发
    # socketserver.ForkingTCPServer 多进程，windows不能使用

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
