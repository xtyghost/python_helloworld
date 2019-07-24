#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 100:
    print(b, end= ',')
    a, b = b, a + b
i = 256*256
print('i 的值为：%d'% i)
print(r'///n/r/t/.')