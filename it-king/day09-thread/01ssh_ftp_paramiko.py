# Author: Peter

import paramiko

# 类似于scp的功能
# scp -rp -P44077  test.txt root@192.168.7.204:/data/
transport = paramiko.Transport(('192.168.7.204', 22))
transport.connect(username='root', password='vskyslv2qq.')
sftp = paramiko.SFTPClient.from_transport(transport)

# sftp.put('test_file/tbdress.log', '/data/tbdress.log')   # 将tbdress.log 上传至服务器 /data/tbdress.log

sftp.get('/data/taglist_46.zip', 'test_file/taglist_46.zip')  # /data/taglist_46.zip 下载到本地 test_file/taglist_46.zip

transport.close()
