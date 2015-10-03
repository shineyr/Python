#为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
#这样，在set_score()方法里，就可以检查参数

class Student(object):
	def get_score(self):
		return self._score;

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value<0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score = value

s = Student()
s.set_score(60) #ok
print(s.get_score())

#s.set_score(999)
#print(s.get_score())  #提示错误

#Python内置的@property装饰器就是负责把一个方法变成属性调用

class Student(object):
	@property
	def score(self):
	    return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value<0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score = value 

#@property的实现比较复杂，我们先考察如何使用。
#把一个getter方法变成属性，只需要加上@property就可以了，
#此时，@property本身又创建了另一个装饰器@score.setter，
#负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
s = Student()
s.score = 60 #ok 实际化为s.set_score(60)
print(s.score)

#注意到这个神奇的@property，我们在对实例属性操作的时候，
#就知道该属性很可能不是直接暴露的，
#而是通过getter和setter方法来实现的。

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student(object):
	@property
	def birth(self):
	    return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
	    return 2015 - self._birth

s = Student()
s.birth = 1991
print(s.age)

#上面的birth是可读写属性，而age就是一个只读属性，
#因为age可以根据birth和当前时间计算出来

#练习
#请利用@property给一个Screen对象加上width和height属性，
#以及一个只读属性resolution：

class Screen(object):
	@property
	def width(self):
	    return self._width	
	
	@width.setter
	def width(self,value):
		self._width = value
	
	@property
	def height(self):
	    return self._height
	@height.setter
	
	def height(self,value):
		self._height = value
	
	@property
	def resolution(self):
	    return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768

print(s.resolution)

	


	
	