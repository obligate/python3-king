# Author: Peter
# 之前的例子都基本都是1对1的消息发送和接收，即消息只能发送到指定的queue里，但有些时候你想让你的消息被所有的Queue收到，类似广播的效果，这时候就要用到exchange了，
# Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息
# 1. fanout: 所有bind到此exchange的queue都可以接收消息，类似于收音机工作方式
#           实时的，如果subscriber离开了就收不到，可以先启动subscriber，然后执行publisher
# 2. direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
# 3. topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
# 　　 表达式符号说明：#代表一个或多个字符，*代表任何字符
#       例：#.a会匹配a.a，aa.a，aaa.a等
#           *.a会匹配a.a，b.a，c.a等
#      注：使用RoutingKey为#，Exchange Type为topic的时候相当于使用fanout　
# 4. headers: 通过headers 来决定把消息发给哪些queue


import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"   # 支持输入message，如果没有输入，默认就是后面的message
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
