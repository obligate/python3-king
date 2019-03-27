# Author: Peter

from urllib import request
import gevent
import time
from gevent import monkey

monkey.patch_all()  # 把当前程序的所有的io操作给我单独的做上标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    # with open("url.html") as f:
    #     f.write(data)
    print('%d bytes received from %s.' % (len(data), url))


# 同步抓取
urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/']
time_start = time.time()
for url in urls:
    f(url)
print("同步cost", time.time() - time_start)

# 异步抓取
# monkey.patch_all()  # 需要在程序开头加上，把当前程序的所有的io操作给我单独的做上标记
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost", time.time() - async_time_start)
