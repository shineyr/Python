__author__ = 'Admin'

# StringIO 在内存中读写str

from io import StringIO
f = StringIO()
print(f.write('hello')) #返回写入字符的长度

#getvalue()方法用于获得写入后的str
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while(True):
    s = f.readline()
    if s == '':
        break
    print(s.strip())


# 字节流IO
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

# 上述写入的不是str，而是经过UTF-8编码的bytes。

# StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())




