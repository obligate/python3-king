# Author: Peter
import pika
import uuid
import time


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        # 声明收消息，只要一收到消息，就调用回调函数on_response
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,  # 发消息的时候约定server执行结果发送到一个新的queue
                                       # 确保发送的命令和服务端返回的结果是一致的，当同一个client发送多条命令的时候,执行有先后的问题，确保发的命令跟服务端返回的结果是一致的，不会乱
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        # 如果没有消息就不阻塞，一直收，直到不为None为止
        # 通过on_response回调函数，收消息
        while self.response is None:
            # 非阻塞版的start_consuming()
            # 没有消息就不收消息，继续执行下面语句，不阻塞
            # 如果有消息，就收消息，调用on_response回调函数，收到消息，此时有消息，循环就结束了
            self.connection.process_data_events()
            print("no message")
            time.sleep(0.5)
        return int(self.response)


# 开始发送
fibonacci_rpc = FibonacciRpcClient()
print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)
