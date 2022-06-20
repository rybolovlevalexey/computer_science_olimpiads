file = open('26_2(1).txt', 'r')
sp = file.read().strip().split('\n')
n, s = map(int, sp[0].split())
del sp[0]
typea = list()
typeb = list()
summa = 0
for elem in sp:
    cost, count, type = elem.split()
    if type == 'A':
        typea.append([int(cost), int(count)])
        summa += (int(cost) * int(count))
    else:
        typeb.append([int(cost), int(count)])
typeb = sorted(typeb)
cntb = 0
money = s - summa
for elem in typeb:
    cost, count = elem
    if cost * count <= money:
        money -= cost * count
        cntb += count
    else:
        for j in range(count, 0, -1):
            if cost * j <= money:
                money -= cost * j
                cntb += j
                break
print(cntb, money)