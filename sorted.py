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

