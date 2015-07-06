#面向对象编程
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000

#(1) 使用dict实现
std1 = {'name' : 'Michael' , 'score':88}
std2 = {'name' : 'Bob' , 'score':81}

def print_score(std):
	print('%s: %s' % (std['name'] , std['score']))	

print_score(std1);
print_score(std2);

#(2) 使用面向对象编程思想实现
class Student(object):
	
	def __init__(self , name , score):
		self.name = name
		self.score = score
		
	def print_score(self):
		print('%s: %s' % (self.name , self.score))
		
bart = Student('Bart Simpson' , 58)
lisa = Student('Lisa Simpson' , 89)
bart.print_score()
lisa.print_score()

