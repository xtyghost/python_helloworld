#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:  %s" % (self.name, self.score))


lisu = Student('lisu', '99')

lisu.print_score()
lisu.print_score()


class Student2(object):

    def __init__(self, name, score):
        self._name = name
        self._score = score
    def print_score(self):
        print("%s:  %s" % (self._name, self._score))


lisu2 = Student2('lisu', '99')

lisu2.print_score()
