# 装饰器
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000

# (1) 变量调用函数对象
def now():
	print("2015-07-03")
	
f = now()

# (2) 函数对象的name属性

print(now.__name__)





