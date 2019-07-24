#!/usr/bin/python3
import time
# 斐波那去函数实现
def fab1(max):
    n,a,b=0,0,1
    while n<max:
        print('->',b,'\r\n')
        a,b=b,a+b
        n=n+1
# 生成器算法实现斐波那契额函数
def fab2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a=b
        n=n+1
        pass
def GeneratorDome():
    t1=time.time();
    maxnum=10000
    fab1(maxnum)
    t2 = time.time();
    print(t2-t1)
    t3=time.time();
    fab2(maxnum)
    t4 = time.time();
    print(t4-t3)
    pass
if __name__=='__main__':
    GeneratorDome()