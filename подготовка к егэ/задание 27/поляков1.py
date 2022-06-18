file = open('27data/51/27-51b.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
nechet = chet = 0
summa = 0
mndl = None
for elem in sp:
    a, b = sorted(map(int, elem.split()))
    summa += a
    if a % 2 == 0:
        chet += 1
    else:
        nechet += 1
    if a % 2 != b % 2 and (mndl is None or mndl > b - a) and b != a:
        mndl = b - a

print(summa)
print(chet, nechet)
summa += mndl
print(summa)