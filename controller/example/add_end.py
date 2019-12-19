# 默认参数必须指向不变参数, 方法里的默认参数相当与匿名成员变量
def add_end(L=[]):
    L.append("END")
    return L


print(add_end())
print(add_end())


# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1, 2, 3))


def person(name, age, **kwargs):
    print('name,%s,age,%s,other,%s' % (name, age, kwargs))


person('Michael',30)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def student(name, age, *args,city,job):
    print(name,age,city,job,args)


student("jack",23,'kk','ww',city='123',job='123')