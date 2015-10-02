__author__ = 'Admin'

# pickle 实现序列化  使用方法dumps

# import pickle
#
# d = dict(name='Bob', age=20, score=88)
# data = pickle.dumps(d)
# print(data)
#
# reborn = pickle.loads(data)
# print(reborn)

import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)

reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

