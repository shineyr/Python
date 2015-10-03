# 回文数是指从左向右 与 从右向左读都是一样的数 如12321 909
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000

# 判断回文数的函数一
def is_palindrome1(n):
	s = str(n)
	size = len(s)
	for i in range(0,size):
		if s[i] != s[-i-1]:
			return False
		else:
			return True
			
# 判断回文数函数二
def is_palindrome2(n):
	s = str(n)
	if s == s[::-1]:
		return True;
	else:
		return False;

# 判断回文数函数三

def is_palindrome3(n):
	return n == int(str(n)[::-1])
		
		
# 求1~1000中的所有回文数

output = filter(is_palindrome3 , range(1 , 1000))
print(list(output))