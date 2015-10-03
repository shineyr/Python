# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

# 先定义一个类
class Student(object):
	pass

s = Student()
s.name = "Michael" #动态给实例绑定一个属性
print(s.name)

# 动态给实例绑定一个方法
def set_age(self , age):
	self.age = age

from types import MethodType
#给实例s绑定一个方法
s.set_age = MethodType(set_age,s)
s.set_age(25) #调用实例方法
print(s.age)

#给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student() #创建新的实例
#s2.set_age(30) #尝试调用方法，会出错


#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self , score):
	self.score = score

Student.set_score = MethodType(set_score , Student)

#给class绑定方法后，所有实例均可调用
s.set_score(100)

print(s.score)

s2.set_score(90)
print(s2.score)



# 限制实例的属性,Python允许在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性

class Student(object):
	__slots__ = ('name' , 'age') #用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Yangrui' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

print(s.name)
print(s.age)
#print(s.score)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)

