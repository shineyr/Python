#(1)在一个list中删掉偶数只留奇数
def is_odd(n):
	return n % 2 == 1
	
print(list(filter(is_odd , [1 , 2 , 3 , 4 , 5 , 6])))

#(2)把一个序列中的空字符串删除

def is_empty(s):
	return s and s.strip()
	
print(list(filter(is_empty , ['A' , '' , 'B' , None , 'C' , ' '])))

