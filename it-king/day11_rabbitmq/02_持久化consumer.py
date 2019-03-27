# Author: Peter
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello_persist', durable=True)


def callback(ch, method, properties, body):
    print("--->", ch, method, properties)
    # time.sleep(30)  # 模拟30s，突然断电的情况，会转发到别的cosumer，需要去掉no_ack=True
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 需要手动发送一个确认消息给producer，接受完毕，可以删除


# 声明开始收消息
channel.basic_consume(callback,  # 如果收到消息，就调用callback函数来处理消息
                      queue='hello_persist',
                      # no_ack=True   # 默认不加no_ack,消息没有处理完毕就不会给producer确认，会转发别的cosumer,处理完毕，producer会删除这条消息
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式开始收消息，会永远收，没有就卡住
channel.start_consuming()
