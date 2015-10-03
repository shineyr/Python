#偏函数
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000

#(1)函数转换
print(int("12345"))

#(2)N进制转换
print(int('12345' , base = 8))
print(int('12345' , base = 16))

#(3)定义转换函数
def int2(x , base=2):
	return int(x,base)
	
print(int2('10000'))
print(int2('10001'))

#(4)使用functools.partial
import functools
int2 = functools.partial(int , base=2)
print(int2('100000'))
print(int2('1010101'))

#(5)参数问题
import functools
max2 = functools.partial(max , 10)

print('max number is：' , max2(3,4,5))



