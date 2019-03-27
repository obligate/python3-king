# Author: Peter
import getpass

_username = 'peter'
_passwd = 'peter'
username = input("username: ")
# passwd = getpass.getpass("passwd: ")  # getpass在pycharm不好用，只能在控制台使用
passwd = input("passwd: ")

if _username == username and _passwd == passwd:
    print('Welcome user {name} login ...'.format(name=username))
else:
    print('Invalid username or password!')

# print(username, passwd)
