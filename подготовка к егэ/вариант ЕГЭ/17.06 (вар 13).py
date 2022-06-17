file = open('27_B (1).txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
summa = 0
mndl = None
for elem in sp:
    a, b, c = sorted(map(int, elem.split()))
    summa += c
    d1 = c - b
    d2 = c - a
    if d1 != 0 and d1 % 109 != 0 and (mndl is None or d1 < mndl):
        mndl = d1
    if d2 != 0 and d2 % 109 != 0 and (mndl is None or d2 < mndl):
        mndl = d2
print(summa, summa % 109)
print(mndl)
print(summa - mndl)