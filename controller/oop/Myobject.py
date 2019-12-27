#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class MyObject(object):
    def __init__(self):
        self.x = 9
        self.y = 8

    def powerX(self):
        return self.x * self.x

    def powerY(self):
        return self.y * self.y


obj = MyObject()
print(hasattr(obj, 'y'))


def power(obj):
    if hasattr(obj, 'powerX'):
        return getattr(obj, 'powerX')
    else:
        return None


fn = power(obj)
print(fn())
