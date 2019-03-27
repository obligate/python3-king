# Author: Peter

import paramiko

# ssh-copy-id   "-p44077 root@192.168.7.204"
# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.7.204', port=22, username='root', password='vskyslv2qq.')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')  # top -bn 1
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err

print(result.decode())

# 关闭连接
ssh.close()
