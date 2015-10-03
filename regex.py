__author__ = 'Admin'
# 在python中使用正则表达式

# 使用转义
s = 'ABC\\-001'
print(s)

# 使用Python的r前缀，无需考虑转义
s = r'ABC\-001'
print(s)

# 使用Python的re模块
import re

# match函数匹配则返回一个Match对象，否则返回none
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式' ,test):
    print('ok')
else:
    print('failed')

# 切分字符串
print('a b  c'.split(' '))

# 用正则表达式处理无法识别空格的问题
print(re.split(r'\s+','a b  c'))

# 无论多少空格，都可以正常分割
print(re.split(r'[\s\,]+' , 'a,b, c d'))
print(re.split(r'[\s\,\;]+' , 'a , b ; c d'))

# 分组，除了简单判断是否匹配，正则表达式还有提取子串的强大功能
# 用（）表示的就是要提取的分组
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
# group(0)代表原始字符串
print(m.group(0))

# group(1) group(2) 代表第1/2...个子串
print(m.group(1))
print(m.group(2))

# 匹配合理时间
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3][0-9])'
             r'\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])'
             r'\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

print(m.groups())

# 贪婪匹配 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$' , '102300').groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

# 用编译后的正则表达式去匹配字符串。

# 预编译正则表达式，提高效率
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，
# 所以调用对应的方法时不用给出正则字符串
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8085').groups())



