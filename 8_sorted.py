#本节介绍的Python内置sorted函数
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000

# python 内置sort函数
print(list(sorted([36 , -5 , 3 , -20 , 56])))

# 为sort函数添加排序规则
print(list(sorted([36 , -5 , 3 , -20 , 56] , key = abs)))

# 为字符串排序
print(list(sorted(['bob', 'about', 'Zoo', 'Credit'])))

# 添加规则，忽略大小写
print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)))

# 添加规则，反向排序
print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower , reverse = True)))

