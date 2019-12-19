# -*- coding: utf-8 -*-

# def createCounter():
#     k = [0]
#
#     def counter():
#         k[0] += 1
#         return k[0]
#
#     return counter

def createCounter():
    """
     create a counter
     """
    k = 0

    def counter():
        nonlocal k
        k += 1
        return k

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print(createCounter.__doc__)


# def log(func):
#     """
#      enhance func ,print log
#     :param func:
#     :return:
#     """
#
#     def wrapper(*args, **kwargs):
#         print('call %s()' % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# mylog = log(counterA)
# print(mylog())
@log('execute')
def now():
    print('2015-3-25')


print(now.__name__)
