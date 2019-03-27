__author__ = "Peter"

# 用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
import hashlib

m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's been a long time since we spoken...")
print(m.hexdigest())

m2 = hashlib.md5()
m2.update("HelloIt's me天王盖地虎".encode(encoding="utf-8"))
print(m2.hexdigest())

s2 = hashlib.sha1()
s2.update(b"HelloIt's me")
print(s2.hexdigest())

# 还不够吊？python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
# 散列消息鉴别码，简称HMAC，是一种基于消息鉴别码MAC（Message Authentication Code）的鉴别机制。使用HMAC时,消息通讯的双方，通过验证消息中加入的鉴别密钥K来鉴别消息的真伪；
# 一般用于网络通信中消息加密，前提是双方先要约定好key,就像接头暗号一样，然后消息发送把用key把消息加密，接收方用key ＋ 消息明文再加密，拿加密后的值 跟 发送者的相对比是否相等，这样就能验证消息的真实性，及发送者的合法性了。

import hmac

h = hmac.new(b"12345", "you are 250你是".encode(encoding="utf-8"))
print(h.digest())
print(h.hexdigest())
