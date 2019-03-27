# Author: Peter
# To illustrate how an RPC service could be used we're going to create a simple client class. It's going to expose a method named call which sends an RPC request and blocks until the answer is received
# fibonacci_rpc = FibonacciRpcClient()
# result = fibonacci_rpc.call(4)
# print("fib(4) is %r" % result)

# 1. 先启动server
# 2. 后启动client
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 1. 收到消息
# 2. 执行命令
# 3. 把命令执行的结果，生产数据并发回给客户端，通过另外一个queue
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,  # 从client传递过来的queue（随机生产的一个queue）
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 开始声明queue，接受客户端传递过来的命令，进行消费
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
print(" [x] Awaiting RPC requests")
channel.start_consuming()
