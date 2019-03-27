# Author: Peter
# 1. 先启动消息生产者，然后再分别启动3个消费者，通过生产者多发送几条消息，你会发现，这几条消息会被依次分配到各个消费者身上
# 是平均的分发
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建一个socket
channel = connection.channel()  # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello_base')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello_base',  # queue名字
                      body='Hello World!',
                      )
print(" [x] Sent 'Hello World!'")
connection.close()
