import functools
import time


def log(func):
    # python的闭包函数，懒加载，几层分装都是懒加载
    @functools.wraps(func)  # 在有些依赖函数签名的需要
    def wrapper(*args, **kw):
        start = time.time();

        kk = func(*args, **kw)
        end = time.time()
        jg = end - start
        print('函数:%s的执行时间是%s' % (func.__name__, jg))
        return kk  # 这里不要在返回func(*args, **kw)了。我们不需要函数now的返回值。反而会执行两次

    return wrapper


@log
def now():
    time.sleep(3)
    print('begin')
    return 'sdf'


print(now())
