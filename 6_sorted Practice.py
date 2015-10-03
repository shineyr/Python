# sorted 练习题
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按名字排序，是tuple的第一元
def by_name(t):
	return t[0]
	
L2 = sorted(L , key = by_name)
print(L2)

# 按成绩排序，是tuple的第二元
def by_score(t):
	return t[1]
	
L2 = sorted(L , key = by_score , reverse = True)
print(L2)


