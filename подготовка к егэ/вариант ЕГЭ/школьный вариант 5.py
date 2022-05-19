file = open('zadanie_27B.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
sp = list(sorted(sp))
ostat = list()
for elem in sp:
    ostat.append(elem % 9)
d = dict()
for i in range(n):
    d[sp[i]] = ostat[i]
for i in range(25):
    print(i, ')', sp[i], ostat[i])