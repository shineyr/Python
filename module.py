# (1)模块学习

'a test module'

__author__ = 'yr'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print("Hello , world!")
	elif len(args) == 2:
		print('Hello , %s!' % args[1])
	else:
		print('Too many arguments!')
		
if __name__ == '__main__':
	test()
	
	
#测试如下

#python module.py

#python module.py yr


#(2)作用域学习

def _private_1(name):
	return 'Hello , %s' % name
	
def _private_2(name):
	return 'Hi , %s' % name
	
def greeting(name):
	if len(name) > 3:
		print(_private_1(name))
	else:
		print(_private_2(name))

greeting('yr')
