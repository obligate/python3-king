# Author: Peter

import paramiko

# 类似于scp的功能
# scp -rp -P44077  test.txt root@192.168.7.204:/data/
private_key = paramiko.RSAKey.from_private_key_file('test_file/id_rsa204.txt')
transport = paramiko.Transport(('192.168.7.204', 22))
transport.connect(username='root', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)

# sftp.put('test_file/tbdress.log', '/data/tbdress.log')   # 将tbdress.log 上传至服务器 /data/tbdress.log

sftp.get('/data/taglist_46.zip', 'test_file/taglist_4611.zip')  # /data/taglist_46.zip 下载到本地 test_file/taglist_46.zip

transport.close()
