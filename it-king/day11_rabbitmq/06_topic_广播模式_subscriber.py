# Author: Peter
# 1. 命令行方式运行subscriber
# python  06_topic_广播模式_subscriber.py  *.info              # 接受info结尾的消息
# python  06_topic_广播模式_subscriber.py  *.error  mysql.*    # 接受error结尾的消息或者mysql开头的消息
# python  06_topic_广播模式_subscriber.py  #                   # 接受所有的广播
# 2. 命令行方式运行publisher
# python  06_topic_广播模式_publisher.py                       # 默认发送anonymous.info,订阅了*.info会收到
# python  06_topic_广播模式_publisher.py  test.error           # 发送test.error,订阅了*.error的会收到
# python  06_topic_广播模式_publisher.py  mysql.info           # 发送mysql.info,订阅了*.info和mysql.*的会收到
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
