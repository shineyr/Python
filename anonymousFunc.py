# 本节介绍Python的匿名函数
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431843456408652233b88b424613aa8ec2fe032fd85a000

# (1) 直接传入匿名函数
print(list(map(lambda x : x*x , [1,2,3,4,5])))


# (2) 匿名函数作为返回值返回
def build(x , y):
	return lambda: x*x + y*y

print(build(2,3)())
