#类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

#__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

class Student(object):
	def __init__(self , name):
		self.name = name

print(Student('Michael'))

# 输出结果 <__main__.Student object at 0x0000000001EEC438>

#定义__str__()方法
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object(name:%s)' % self.name

print(Student('Michael'))

#输出结果 Student object(name:Michael)

#不用print打印结果仍然如第一种，因为直接显示变量调用的不是__str__()，而是__repr__()，
#两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
#也就是说，__repr__()是为调试服务的

#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，

class Student(object):
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'Student object (name = %s) ' % self.name

	__repr__ = __str__


#如果一个类想被用于for ... in循环，类似list或tuple那样，
#就必须实现一个__iter__()方法，该方法返回一个迭代对象，
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
#直到遇到StopIteration错误时退出循环。

#我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):
	def __init__(self):
		self.a , self.b = 0 , 1 #一次性初始化两个计数器

	def __iter__(self):
		return self #实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a , self.b = self.b , self.a + self.b
		if(self.a > 1000): #退出循环条件
			raise StopIteration();
		return self.a #返回下一个值

for n in Fib():
	print(n)

#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
	def __getitem__(self,n):
		a , b = 1 , 1
		for x in range(n):
			a , b = b , a+b
		return a

f = Fib()
print(f[0])
print(f[1])

#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])

print(f[:10])

#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
# 只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
	def __init__(self , name):
		self.name = name

	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Michael')
s()

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(max))
print(callable([1,2,3]))
