val = 9

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(val))


# 把递归改为尾递归 ，    编译器和解析器会对尾递归进行优化，不会发生栈溢出
# 尾递归指，在返回时返回函数本身，且不能有表达式
def fact2(n, result=1):
    if n == 1:
        return result
    result *= n
    return fact2(n - 1, result)
print(fact2(val))