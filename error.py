#高级语言通常都内置了一套try...except...finally...的错误处理机制

try:
	print('try...')
	r = 10 / 2
	print('result' , r)
except ZeroDivisionError as e:
	print('except' , e)
finally:
	print('finally')
print('END')
#如果有错误，错误语句不会执行，执行捕捉异常语句，以及finally语句
#如果没有错误，try完整执行，不执行捕捉异常语句，但是finally如果有，
#则一定会被执行，可以没有finally语句


#下面错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

#此外，如果没有错误发生，可以在except语句块后面加一个else，
#当没有错误发生时，会自动执行else语句：

try:
	print('try...')
	r = 10 / int('2')
	print('result' , r)
except ValueError as e:
	print('ValueError' , e)
except ZeroDivisionError as e:
	print('ZeroDivisionError' , e)
else:
	print('no error')
finally:
	print('finally...')
print('END')

#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
#比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，
#只要main()捕获到了，就可以处理：

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		return bar('0')
	except Exception as e:
		print('error' , e)
	else:
		print('no error')
	finally:
		print('finally')

#调用main函数
print(main())
print('end')

#错误堆栈
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，
#打印一个错误信息，然后程序退出
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s) * 2

def main():
	return bar('0')

#print(main())
print('END')

#记录错误
#如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，
#但程序也被结束了。既然我们能捕获错误，
#就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        return bar('0')
    except Exception as e:
        logging.exception(e)

print(main())
print('END')