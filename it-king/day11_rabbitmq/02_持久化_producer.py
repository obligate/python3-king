# Author: Peter
# 1. 先启动消息生产者，然后再分别启动3个消费者，通过生产者多发送几条消息，你会发现，这几条消息会被依次分配到各个消费者身上
# 2. 队列持久化,不是消息持久化,需要在生产者和消费者队列声明的时候都需要加上, durable=True
# channel.queue_declare(queue='hello', durable=True)
# 3. 消息持久化，在生产者消息发布的时候加上delivery_mode = 2
# channel.basic_publish(exchange='',
#                       routing_key="task_queue",
#                       body=message,
#                       properties=pika.BasicProperties(
#                          delivery_mode = 2, # make message persistent
#                       ))
#
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建一个socket
channel = connection.channel()  # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello_persist', durable=True)

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello_persist',  # queue名字
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()
