__author__ = 'Admin'

f  = open("E:/projects/Python/test.txt",'r')

print(f.read())

f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，
# 后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，
# 我们可以使用try ... finally来实现.

try:
    f = open('E:/projects/Python/test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

# Python引入了with语句来自动帮我们调用close()方法
with open('E:/projects/Python/test.txt','r') as f:
    print(f.read());


# 打开二进制文件，用rb即可
f = open('E:/projects/Python/coder.png','rb')
print(f.read())
f.close();

# 写文件
f = open('E:/projects/Python/test.txt' , 'w')
f.write('I am Yang rui , hello!');

f.close();



