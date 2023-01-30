# change_xshell_cpolar_ip
修改xshell的连接文件，不用每次都去cpolar上面复制ssh的账户或者密码


目前有2个接口，一个请求set-cookie，请求回cookie
第二个请求页面数据，cpolar返回的是一整个html页面，使用正则解析


【目前缺陷】
1、一个接口需要22秒左右时间，非常慢
2、必须网页登录一下，大约有24小时的有效期，期间都可以使用登录
