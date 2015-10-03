# 访问限制
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000

# 变量前加__就成为了私有变量
class Student(object):
	def __init__(self , name , score):
		self.__name = name
		self.__score = score
	
	def set_name(self , name):
		self.__name = name
		
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
	
	def set_score(self , score):
		if 0<= score <= 100 :
			self.__score = score
		else:
			raise ValueError("bad score")
		
	def print_score(self):
		print("%s: %s" % (self.__name , self.__score))
		
	def get_grade(self):
		if self.__score >= 90 :
			return 'A'
		elif self.__score >= 80 :
			return 'B'
		else :
			return 'C'

			
bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)

bart.print_score();
print('bart 成绩级别：' , bart.get_grade());
