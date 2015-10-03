# 继承和多态
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000

# (1) 继承
class Animal(object):
	def run(self):
		print('Animal is running...')
		
class Dog(Animal):
	pass

class Cat(Animal):
	pass
	
print('第一次运行:\n')	
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 重写函数
class Dog(Animal):
	def run(self):
		print('Dog is running...')
		
class Cat(Animal):
	def run(self):
		print('Cat is running...')

print('再次运行:\n')	
dog = Dog()
dog.run()

cat = Cat()
cat.run()