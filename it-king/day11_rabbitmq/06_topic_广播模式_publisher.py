# Author: Peter
# Although using the direct exchange improved our system, it still has limitations - it can't do routing based on multiple criteria.
# In our logging system we might want to subscribe to not only logs based on severity, but also based on the source which emitted the log. You might know this concept from the syslog unix tool, which routes logs based on both severity (info/warn/crit...) and facility (auth/cron/kern...).
# That would give us a lot of flexibility - we may want to listen to just critical errors coming from 'cron' but also all logs from 'kern'.
#
# To receive all the logs run:
#   python receive_logs_topic.py "#"
# To receive all logs from the facility "kern":
#   python receive_logs_topic.py "kern.*"
# Or if you want to hear only about "critical" logs:
#   python receive_logs_topic.py "*.critical"
# You can create multiple bindings:
#   python receive_logs_topic.py "kern.*" "*.critical"
# And to emit a log with a routing key "kern.critical" type:
#   python emit_log_topic.py "kern.critical" "A critical kernel error"
# 　　
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

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
