file = open('27-11b.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
summa = 0
ost = dict()
for elem in sp:
    a, b, c = sorted(map(int, elem.split()))
    summa += c
    d1 = c - b
    d2 = c - a
    if d1 % 8 not in ost or (d1 % 8 in ost and ost[d1 % 8] > d1):
        ost[d1 % 8] = d1
    if d2 % 8 not in ost or (d2 % 8 in ost and ost[d2 % 8] > d2):
        ost[d2 % 8] = d2
print(summa, summa % 8)
print(ost)