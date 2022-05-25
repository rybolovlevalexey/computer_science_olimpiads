file = open('26 (1).txt', 'r')
sp = file.read().strip().split('\n')
n, m = map(int, sp[0].split())
del sp[0]
summa = 0
izdA = dict()

for elem in sp:
    cost, colvo, tip = elem.split()
    cost = int(cost)
    colvo = int(colvo)
    if tip == 'B':
        summa += (colvo * cost)
    else:
        if cost in izdA:
            izdA[cost] += colvo
        else:
            izdA[cost] = colvo

cntA = 0
for key in sorted(izdA.keys()):
    if summa + key * izdA[key] <= m:
        summa += key * izdA[key]
        cntA += izdA[key]
    else:
        for colichestvo in range(izdA[key], 0, -1):
            if summa + key * colichestvo <= m:
                cntA += colichestvo
                summa += key * colichestvo
print(cntA, m - summa)