l = input('please enter a number:')

def triangles(l):

    L = [1]

    n = 0

    while n < int(l):

        yield L

        L1 = L[:]

        for i in range(1, len(L)):

            L1[i] = L[i-1]+L[i]

        L1.append(1)

        L = L1[:]

        n+=1

result = []

for i in triangles(l):

    result.append(i)

for t in result:

    print(t)