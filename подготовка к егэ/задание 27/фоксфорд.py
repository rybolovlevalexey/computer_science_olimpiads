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
    if is_prost(elem) and len(str(elem)) == 3:
        ind.append(i)
mxsm = 0
poz1 = 0
poz2 = 5
print(ind)
while True:
    if poz1 > 0 and poz2 + 1 < len(ind):
        i1 = ind[poz1 - 1] + 1
        i2 = ind[poz2 + 1]
        srez = sp[i1: i2]
    else:
        i1 = ind[poz1]
        i2 = ind[poz2]
        srez = sp[i1: i2]
    summa = sum(srez)
    coutn = 0
    for elem in srez:
        if is_prost(elem) and len(str(elem)) == 3:
            coutn += 1
    print(coutn)
    # ......
    if summa > mxsm:
        mxsm = summa
    poz2 += 5
    if poz2 >= len(ind):
        poz1 += 1
        poz2 = poz1 + 5
        if poz1 >= len(ind) or poz2 >= len(ind):
            break
print(mxsm)