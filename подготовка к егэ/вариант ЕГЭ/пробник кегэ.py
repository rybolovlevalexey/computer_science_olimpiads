file = open('27_A (2).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
mxsm = 0
mndl = 0
for i in range(n - 1):
    for j in range(i + 1, n + 1):
        srez = sp[i: j]
        summa = sum(filter(lambda x: x % 2 == 0, srez))
        if summa % 16 == 0 and summa > mxsm:
            mxsm = summa
            mndl = len(srez)
        elif summa % 16 == 0 and summa == mxsm and len(srez) < mndl:
            mndl = len(srez)
print(mndl)