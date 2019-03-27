## JsonP本质
【http://www.cnblogs.com/wupeiqi/articles/5703697.html】
+ 由于浏览器具有同源策略（阻止Ajax请求，无法阻止<script src=''></script>）
巧妙：
    + 创建script标签
    + src=远程地址
    + 返回的数据必须是js格式
    + **只能发Get请求，jquery内部把post请求转换成Get请求**
+ 同源策略对应以下使用无法阻止
    + script src
    + a href
    + iframe