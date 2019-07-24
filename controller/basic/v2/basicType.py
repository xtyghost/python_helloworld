#!/usr/bin/python3

a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)
# Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
a,b,c,d=20,5.5,True,4+3j
print('a','===========',type(a))
print('b','===========',type(b))
print('c','===========',type(c))
print('d','===========',type(d))
a=111
print(isinstance(a,int))

# str处理
str='Runoob'
print(str)
print(str[0:-1])
print(str[0:])
print(str[2:5])