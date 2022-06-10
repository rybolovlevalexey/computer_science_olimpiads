file = open('27-A_demo.txt', 'r')
s = file.read().strip().split('\n')
n = int(s[0])
del s[0]
sp = list()
summa = 0
mndl = None
for elem in s:
    a, b = map(int, elem.split())
    sp.append(sorted([a, b]))
    summa += max(a, b)
    if (mndl is None or abs(a - b) < mndl) and min(a, b) % 3 != 0:
        mndl = abs(a - b)
sp = sorted(sp, key= lambda x: x[0])
print(summa, summa % 3, mndl)
ans = summa - mndl
print(ans, ans % 3)