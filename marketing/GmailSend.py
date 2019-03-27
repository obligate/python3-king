# Author: Peter
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 带附件的
from email.header import Header

mail_host = "smtp.gmail.com"  # 设置服务器
gmail_user = "abelardbaker1821@gmail.com"  # 用户名
gmail_password = "1234ABcd"  # 口令

def send_simple():
    sent_from = gmail_user
    to = ['peter@tidebuy.net']  # 接收邮件

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("Peter", 'utf-8')                      # Peter<tlzsemsys@gmail.com>
    # message['To'] = Header("测试", 'utf-8')                        # 测试<peter@tidebuy.net>

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message.as_string())
        server.close()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)


def send_html():
    sent_from = gmail_user
    to = ['peter@tidebuy.net']  # 接收邮件

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://seal.tidebuy.net:9200">这是一个链接</a></p>
    """

    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("Peter", 'utf-8')  # Peter<tlzsemsys@gmail.com>
    # message['To'] = Header("测试", 'utf-8')       # 测试<peter@tidebuy.net>

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message.as_string())
        server.close()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)


def send_attachment():
    sent_from = gmail_user
    to = ['peter@tidebuy.net']  # 接收邮件

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Peter", 'utf-8')  # Peter<tlzsemsys@gmail.com>
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是Python 邮件发送测试……', 'html', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt.txt 文件
    att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    message.attach(att2)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message.as_string())
        server.close()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)


if __name__ == '__main__':
    # send_simple()
    send_html()
    # send_attachment()
