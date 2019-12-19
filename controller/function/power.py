def power(x,n = 2):
    s =1
    while n > 0:
        n = n - 1
        s = s * x
        if n == 1:
            pass
    return s

print(power(10))

