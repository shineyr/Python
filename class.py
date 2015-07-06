# 类和实例
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431864715651c99511036d884cf1b399e65ae0d27f7e000

class Student(object):
	def __init__(self , name , score):
		self.name = name
		self.score = score
	
	def print_score(self):
		print("%s: %s" % (self.name , self.score))
		
	def get_grade(self):
		if self.score >= 90 :
			return 'A'
		elif self.score >= 80 :
			return 'B'
		else :
			return 'C'

bart = Student('Bart' , 59)
jack = Student('Jack' , 90)

bart.print_score();
print('bart 成绩级别：' , bart.get_grade());

jack.print_score();
print('jack 成绩级别：' , jack.get_grade());

