file = open('27-B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
sp = sorted(list(map(int, sp)))[::-1]
ostatki = list()
for elem in sp:
    ostatki.append(elem % 3)
print(ostatki[:8])
print(sp[:8])
d = dict()
for i in range(n):
    d[sp[i]] = ostatki[i]
#print(d)
print(sp[0] + sp[2] + sp[5], (sp[0] + sp[2] + sp[5]) % 3)
print(sp[1] + sp[3] + sp[4], (sp[1] + sp[3] + sp[4]) % 3)