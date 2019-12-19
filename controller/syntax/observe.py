# 返回函数，并不直接返回结果
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 25, 7, 213, 7)
print('defination of  sum function ======= ', f)
print(
    f()
)

f1 = lazy_sum(12, 23)
f2 = lazy_sum(12, 23)
print(f1.__eq__(f2))
print(f1 == f2)
