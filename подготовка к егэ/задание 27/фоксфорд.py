file = open('27B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
summa = 0
ostatki = dict()
for elem in sp:
    a, b = sorted(map(int, elem.split()))
    summa += b
    d = b - a
    if b - a == 6:
        print('here')
    if d % 5 in ostatki and ostatki[d % 5] > d:
        ostatki[d % 5] = d
    if d % 5 not in ostatki:
        ostatki[d % 5] = d
print(summa)
print(ostatki)