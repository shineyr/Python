__author__ = 'Admin'

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
# 目的是为了发现原始数据是否被人篡改过。

import hashlib
md = hashlib.md5()

md.update('how to use md5 in python hashlib?'.encode('utf-8'))

print(md.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，
# 通常用一个32位的16进制字符串表示

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('pthon hashlib?'.encode('utf-8'))

print(sha1.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
#
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，
# 而且摘要长度更长。