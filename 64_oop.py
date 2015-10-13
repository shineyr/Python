__author__ = 'Admin'

# 学习网址 http://www.yiibai.com/python/python_classes_objects.html

# 本节是Python的面向对象补充学习

class Employee:
    # 'Common base classes for all emplyees'
    empCount = 0

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # python中的静态方法，需要使用@标识符 也叫 python 修饰器 显示说明
    @staticmethod
    def displayCount():
        print("Total Employee is " , Employee.empCount)

    def displayEmployee(self):
        print('Name: ' , self.name , ' , salary :' , self.salary )


emp1 = Employee('zata' , 2000)
emp2 = Employee('Manni' , 3000)

emp1.displayEmployee()
emp2.displayEmployee()

Employee.displayCount()

# 添加对象属性，只为当前对象加上了该属性
emp1.age = 20
print(emp1.age)
del emp1.age

# 除了使用正常的语句来访问属性，可以使用以下函数：
#
# getattr(obj, name[, default]) : 访问对象的属性。
#
# hasattr(obj,name) : 检查一个属性是否存在。
#
# setattr(obj,name,value) : 设置一个属性。如果属性不存在，那么它将被创建。
#
# delattr(obj, name) : 要删除一个属性。


# 内置类属性
# 每个Python类会继续并带有内置属性，他们可以使用点运算符像任何其他属性一样来访问：
#
# __dict__ : 字典包含类的命名空间。
#
# __doc__ : 类的文档字符串，或None如果没有定义。
#
# __name__: 类名称。
#
# __module__: 在类中定义的模块名称。此属性是在交互模式其值为“__main__”。
#
# __bases__ : 一个可能是空的元组包含了基类，其在基类列表出现的顺序。

class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def displayCount():
        print("Total Employee %d " , Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name , " , Salary: " , self.salary)


print("Employee.__doc__: " , Employee.__doc__)
print("Employee.__name__: " , Employee.__name__)
print("Employee.__module__: ", Employee.__module__)
print("Employee.__dict__: ", Employee.__dict__)
print("Employee.__bases__: ", Employee.__bases__)



# 类继承
# 不用从头开始，可以通过上面列出的括号父类的新类名后，
# 从一个已经存在的类派生它创建一个类。

# 子类继承父类的属性，可以使用父类的这些属性，就好像它们是在子类中定义的一样。
# 子类也可以覆盖父类的数据成员和方法。

class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("calling parent method")

    def setAttr(self , attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("parent attribute:" , Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

c = Child()

c.childMethod() #只会调用子类自身的构造函数，不会调用父类的构造函数

c.parentMethod()

c.setAttr(200)

c.getAttr()

# 可以使用issubclass()或isinstance()函数来检查两个类和实例的关系。
#
# issubclass(sub, sup) 如果给定的子类子确实是超sup的子类布尔函数返回true。
#
# isinstance(obj, Class) 如果obj是Class类的实例，或者是类的一个子类的实例布尔函数返回true

print(issubclass(Child , Parent))

print(isinstance(c , Child))

print(isinstance(c , Parent))

p = Parent()

print(isinstance(p , Child))
