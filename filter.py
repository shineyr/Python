# 本节介绍Python内置filter
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000

#(1)在一个list中删掉偶数只留奇数
def is_odd(n):
	return n % 2 == 1
	
print(list(filter(is_odd , [1 , 2 , 3 , 4 , 5 , 6])))

#(2)把一个序列中的空字符串删除

def is_empty(s):
	return s and s.strip()
	
print(list(filter(is_empty , ['A' , '' , 'B' , None , 'C' , ' '])))

