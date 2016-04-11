#(1)构造一个从3开始的奇数序列，是一个无限序列的生成器
def _odd_order():
    n = 1
    while True:
        n = n + 2
        yield n

#(2)定义一个筛选函数
def _not_divisible(n):
    return lambda x : x % n > 0

#(3)定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_order() #初始序列
    while True:
        n = next(it)    #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)   #返回新序列

#(4)打印100以内的所有素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break
