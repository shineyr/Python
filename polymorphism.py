# 多态
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000

class Animal(object):
	def run(self):
		print('Animal is running...')
		
class Dog(Animal):
	def run(self):
		print('Dog is running...')
		
class Cat(Animal):
	def run(self):
		print('Cat is running...')
		
a = list() #a是list类型
b = Animal() #b是Animal类型
c = Dog() #c是Dog类型

print('a是list类型吗？' , isinstance(a , list))
print('b是Animal类型吗？' , isinstance(b , Animal))
print('c是Dog类型吗？' , isinstance(c , Dog))
print('c是Animal类型吗？' , isinstance(c , Animal))
print('b是Dog类型吗？' , isinstance(b , Dog))

#增加一个多态函数,实现对扩展开放，对修改关闭的开闭原则
def run_twice(animal):
	animal.run()
	animal.run()
	
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

	
	
