# sorted 练习题

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


