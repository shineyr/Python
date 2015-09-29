#实例属性和类属性

#由于Python是动态语言，根据类创建的实例可以任意绑定属性。

#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
	def __init__(self , name):
		self.name = name

s = Student('Bob')
s.score = 90

#但是，如果Student类本身需要绑定一个属性呢？可以直接在
#class中定义属性，这种属性是类属性，归Student类所有：

class Student(object):
	name = 'Student'

s = Student() #创建实例s
print(s.name) #打印name属性，因为实例没有name属性，所以会继续查找类的name属性

#打印类的name属性
print(Student.name)

#给实例绑定name属性
s.name = 'Michael'
print(s.name)

#此时类属性并没有消失，用Student.name仍然可以访问
print(Student.name)

#删除实例的name属性
del s.name

print(s.name)



