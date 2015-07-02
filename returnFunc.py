# 本节介绍Python中的返回函数 
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000

# (1) 可变参数的求和
def calc_sum(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print(calc_sum(1,3,4,5,6,7,8))

# (2) 返回求和函数
def lazy_sum(*args):
	def sum():
		result = 0
		for i in args:
			result += i
		return result
	return sum

f = lazy_sum(1 , 3, 4, 5 , 6)
print(f) #此时返回函数
print(f()) #此时返回求和结果

# (3) 闭包问题
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1 , f2 , f3 = count()
# 全部都是9！原因就在于返回的函数引用了变量i，
# 但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9。
print('f1() = ' , f1())
print('f2() = ' , f2())
print('f3() = ' , f3())

# (4) 立即执行闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
	
f1 , f2 , f3 = count()
print('f1() = ' , f1())
print('f2() = ' , f2())
print('f3() = ' , f3())

# (5) 用lambda函数缩短代码
def count():
    def f(j):
        return lambda :j*j
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1 , f2 , f3 = count()
print('f1() = ' , f1())
print('f2() = ' , f2())
print('f3() = ' , f3())	


