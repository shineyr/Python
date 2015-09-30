class Animal(object):
    pass
#正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

#现在，我们要给动物再加上Runnable和Flyable的功能，
#只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog
class Dog(Mammal, Runnable):
    pass

#对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable):
    pass

#通过多重继承，一个子类就可以同时获得多个父类的所有功能。

#在设计类的继承关系时，通常，主线都是单一继承下来的，
#例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
#通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
#再同时继承Runnable。这种设计通常称之为MixIn

#为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
#类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，
#让某个动物同时拥有好几个MixIn：

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

#小结

#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

#只允许单一继承的语言（如Java）不能使用MixIn的设计。