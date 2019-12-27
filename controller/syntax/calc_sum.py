def calc_sum(*args):
    ax = 0
    for n in args:
        args += n
    return ax


def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
    ax += n
        return ax

    return sum1


inner_sum = lazy_sum(1, 2, 3, 6, 9, 10)
print(inner_sum)
print(inner_sum())
