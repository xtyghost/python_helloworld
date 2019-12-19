L = ['Michael', 'Sarah', "Tracy", 'Bob', 'Jack']

print(L[0:3])
print(L[range(4).start])
R = list(range(100))
print(R)

print(R[-10:])

print(R[:10:2])
print(R[:10:3])
print(R[::5])

d = {'a': 1, 'b': 2, 'c': 3}
# dict迭代，默认迭代key，可以使用for   value in d.values()
for value in d:
    print(d[value])

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

print([x * x for x in range(1, 11) if x % 2 == 0 if x != 4])
for k, v in d.items():
    print(k, "==", v)
