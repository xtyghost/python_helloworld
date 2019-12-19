def _prime_number():
    n = 1
    while True:
        n += 2
        yield n


prime = _prime_number()

print(next(prime))
print(next(prime))
print(next(prime))


def _not_divisiable(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _prime_number()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n), it)


for n in _prime_number():
    if n < 1000:
        print(n)
    else:
        break
