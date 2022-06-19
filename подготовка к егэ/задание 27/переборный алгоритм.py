def is_prost(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

file = open('27A (1).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
mxsm = 0
n = sp[0]
del sp[0]
for i in range(n - 1):
    for j in range(i + 1, n):
        srez = sp[i: j]
        prcount = 0
        for elem in srez:
            if len(str(elem)) == 3 and is_prost(elem):
                prcount += 1

        if prcount % 6 == 0 and prcount > 0:
            summa = sum(srez)
            if summa > mxsm:
                mxsm = summa
print(mxsm)