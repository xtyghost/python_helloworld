#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime


class Student(object):
    def __init__(self, name, birth=2000):
        self.name = name
        self.birth = birth

    @property
    def birth(self):
        return self.birth

    @birth.setter
    def birth(self, value):
        self.birth = value

    @property
    def age(self):
        return 2020 - self.birth



lisu = Student('lisu')

lisu.birth = 1995
print(lisu.age)
