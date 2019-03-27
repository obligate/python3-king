## Refer
+ [install](https://www.cnblogs.com/jpfss/p/9009607.html)
+ [erlang](http://www.erlang.org/downloads)
+ [rabbitmq](http://www.rabbitmq.com/install-windows.html)

## windows 安装
### erlang安装
+ [erlang](http://www.erlang.org/downloads)
### 修改环境变量
+ 1添加系统环境变量ERLANG_HOME，值为安装目录. 
+ 2修改系统环境变量Path,在PATH变量中添加`%ERLANG_HOME%\bin`
+ 3重启电脑后，在控制台输入 erl,如果出现类似`Eshell V6.1 (abort with ^G)`字样，说明安装成功。
### rabbitmq安装
+ [rabbitmq](http://www.rabbitmq.com/install-windows.html)
### 运行服务
rabbitMq默认自启动 
可以修改rabbitmq的配置文件，也可以用默认配置运行。
+ 在开始菜单栏里可以看到运行指令reinstall/remove/start/stop 
+ 或者直接打开RabbitMQ Command Prompt命令框rabbitmq-service start
+ 通过开始菜单，进入mq的Prompt command（sbin dir），
    + Rabbitmq 管理插件启动，可视化界面,
        + 开启`rabbitmq-plugins enable rabbitmq_management`
        + 关闭`rabbitmq-plugins disable rabbitmq_management`
    + 本地访问：[localhost](http://localhost:15672/) 登录，用户名密码都是guest 
    + `http://www.rabbitmq.com/devtools.html#python-dev`
+ 服务命令
```
rabbitmq-service install 安装服务
rabbitmq-service start 开始服务
Rabbitmq-service stop  停止服务
Rabbitmq-service enable 使服务有效
Rabbitmq-service disable 使服务无效
rabbitmq-service help 帮助
```
### 配置权限
```
# 首先在rabbitmq server上创建一个用户
sudo rabbitmqctl  add_user peter qwe123
# 同时还要配置权限，允许从外面访问 
sudo rabbitmqctl set_permissions -p / peter ".*" ".*" ".*" 
```
+ set_permissions [-p vhost] {user} {conf} {write} {read}
    + vhost  The name of the virtual host to which to grant the user access, defaulting to /.
    + user The name of the user to grant access to the specified virtual host.
    + conf  A regular expression matching resource names for which the user is granted configure permissions.
    + write A regular expression matching resource names for which the user is granted write permissions.
    + read  A regular expression matching resource names for which the user is granted read permissions.

## 常用命令
``` 
切换到rabbit的安装目录，例如： D:\Software\rabbitMQ\rabbitmq_server-3.7.7\sbin
rabbitmqctl.bat   list_queues             # 获取mq中的队列个数和消息数目
```

## Redis
`pip install redis ` 安装redis
```
set name peter
get name 
keys *
set name peter ex 2    # 2秒后失效
```