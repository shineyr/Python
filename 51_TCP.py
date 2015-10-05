__author__ = 'Admin'

# (1)客户端编程

# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn' , 80)) # 参数是一个tuple

# 建立连接后，发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
    data = b''.join(buffer)

# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，
# 因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环

# 关闭连接
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，
# 把HTTP头打印出来，网页内容保存到文件

header , html = data.split(b'\r\n\r' , 1)
print(header.decode('utf-8'))

# 把接收到的数据写入文件
with open('sina.html' , 'wb') as f:
    f.write(html)



