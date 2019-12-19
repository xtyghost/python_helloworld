classmates = ['Michael', 'Bod', 'Tracy']
classmates.reverse()
print(classmates)

ty = ['python', 'java', ['asp', 'jsp'], 'scheme']
print('%s\'length is %d' % (ty, len(ty)))

# tuple
t = (2, 1)
print('t[0] is %d' % t[0])

t1 = (1)
print(t1)
print((1,))
print(type((['sdf', 'dsf'],)))
print(type(()))


# foreach
def foreach(items):
    for item in items:
        if isinstance(item, list):
            foreach(item)
        else:
            print(item)


foreach(ty)
