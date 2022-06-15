file = open('27-32b.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
summa = 0
ost = dict()
for elem in sp:
    a, b, c = sorted(map(int, elem.split()))
    summa += a
    d1 = c - a
    d2 = b - a
    if (d1 % 11 in ost and ost[d1 % 11] > d1) or d1 % 11 not in ost:
        ost[d1 % 11] = d1
    if (d2 % 11 in ost and ost[d2 % 11] > d1) or d2 % 11 not in ost:
        ost[d2 % 11] = d2
print(summa, summa % 11)
for key in sorted(ost.keys()):
    print(key, ost[key])