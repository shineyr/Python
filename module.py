# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000

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
