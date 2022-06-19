def is_prost(x):
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return False
    return True

file = open('27A (1).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
ind = list()
for i in range(n):
    elem = sp[i]
    if is_prost(elem):
        ind.append(i)
mxsm = 0
poz1 = 0
poz2 = 6

while True:
    i1 = ind[poz1]
    i2 = ind[poz2]
    summa = sum(sp[i1: i2])
    print(sp[i1: i2])
    if summa > mxsm:
        mxsm = summa
    poz2 += 6
    if poz2 >= len(ind):
        poz1 += 1
        poz2 = poz1 + 6
        if poz1 >= len(ind) or poz2 >= len(ind):
            break
print(mxsm)