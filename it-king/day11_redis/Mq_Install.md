## Redis
+ [知识](http://www.cnblogs.com/wupeiqi/articles/5132791.html)
`pip install redis ` 安装redis
### String操作
```
set name peter
get name 
keys *
set name peter ex 2    # 2秒后失效
set name peter nx
set name peter xx
select 2               # 切换一个数据库
keys * 
help mset
mset n1 peter a1 22
mget n1 a1
keys * 
get n1
get a1
getset n1 jack      # 设置新值并返回原来的值
getrange n1 0 2     # 字符串切片，返回jac
setrange n2 0 |  
get n2
set n4 a  
bitcount n4         # 返回3，表示在8个bit为中，有3个是1，5个是0
setbit n4 10 1
bitcount n4         # 返回4
get n4
# 统计在线用户个数，可以通过设置对应的用户id为1，例如
setbit n5 1000 1   # id=1000的用户过来了，设置为1
setbit n5 55   1   # id=55的用户过来了，设置为1
bitcount n5        # 统计在线用户的数量是2
getbit n5 55       # 判断id=55的用户是否在线，在线返回1，不在线返回0
# 计时器
incr login_users   # 自增1   
decr login_users   # 自减1
append name huang
get name 
```
### hash操作
```
hset info name peter
hset info age 23
hset info id 1234
hgetall info
hget info name
hkeys info
hvals info 
hmset info2 k1 1 k2 2 
hmget info2 k1 k2 
hlen info 2 
hexists info2 k2    
hincrby info2 k2 1 
hscan info2 0 match k*
```
### list操作
```
lpush names peter lisa larry candy
lrange names 0 -1
rpush names peter lisa larry candy
lrange names 0 -1
llen names
```

### 发布订阅
```
subscribe fm104.5               # 订阅频道
publish fm104.5 hello           # 发布广播消息
publish fm104.5 "how are you"   
```
