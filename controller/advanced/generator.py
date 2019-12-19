def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(6)
print(next(g))

while True:
    try:
        x = next(g)
        print('g==%d' % x)
    except StopIteration as e:
        print("generator return value:", e.value)
        break
    else:
        pass
