#!/usr/bin python3

# 从wsgiref模块导入
from wsgiref.simple_server import make_server
from hello import application

# 创建一个服务器，IP地址为空，端口是8000处理函数是application
httpd = make_server('' , 8000 , application)
print('Serving HTTP on port 8000...')

#开始监听HTTP请求
httpd.serve_forever()


