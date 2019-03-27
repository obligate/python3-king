## Refer
[icon](https://fontawesome.com/icons?d=gallery)


## js 函数
### 普通函数
function func(){}
### 匿名函数
function(arg){console.log(arg);}
### 自执行函数(创建函数并自动执行函数)
(function(arg){ console.log(arg)})(1);

## json 序列化及转义[refer](http://www.cnblogs.com/wupeiqi/articles/5602773.html)
+ JSON.stringify() 将对象转换成字符串 
```
li = [1,2,3]
s = JSON.stringify(li)
obj = JSON.parse(s)
```
+ JSON.parse()     将字符串转换为对象类型
+ 转义
```
转义
decodeURI( )                   URl中未转义的字符
decodeURIComponent( )   URI组件中的未转义字符
encodeURI( )                   URI中的转义字符
encodeURIComponent( )   转义URI组件中的字符
escape( )                         对字符串转义
unescape( )                     给转义字符串解码
URIError                         由URl的编码和解码方法抛出
```
[自动登录](http://www.cnblogs.com/wupeiqi/articles/5354900.html)