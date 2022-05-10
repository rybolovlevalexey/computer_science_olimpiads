file = open('27-A.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
sp = sorted(list(map(int, sp)))[::-1]
ostatki = list()
for elem in sp:
    ostatki.append(elem % 3)
#print(ostatki)
#print(sp)
d = dict()
for i in range(n):
    d[sp[i]] = ostatki[i]
print(d)