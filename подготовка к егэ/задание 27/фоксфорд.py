file = open('27_3B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
summa = 0
mndl = None
for elem in sp:
    a, b, c = sorted(map(int, elem.split()))
    summa += c
    if b % 5 != 0 and (mndl is None or c - b < mndl) and c - b != 0:
        mndl = c - b
    if a % 5 != 0 and (mndl is None or c - a < mndl) and c - a != 0:
        mndl = c - a
print(summa)
print(mndl)
if summa % 5 == 0:
    print(summa - mndl)