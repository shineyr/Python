# 用filter 求素数程序
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000

# 先构造一个从3开始的奇数序列

def _odd_iter():
	n=1
	while True:
		n = n + 2
		yield n
		
# 定义一个筛选函数

def _not_divisible(n):
	return lambda x : x%n > 0
		
# 最后定义一个生成器，不断返回下一个素数

def primes():
	yield 2
	it = _odd_iter() #初始序列
	while True:
		n = next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n) , it)
		
# 打印1000以内的素数

for n in primes():
	if n < 1000:
		print(n)
	else:
		break

