#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

# 测试:
bart = Student('Bart', 'male')
print(bart._Student__gender)
print(dir(bart))
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
