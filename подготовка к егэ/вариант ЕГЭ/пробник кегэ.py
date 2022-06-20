file = open('27_A (2).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
mxsm = 0
mndl = 0
ind = list()
for i in range(n):
    elem = sp[i]
    if elem % 2 == 0:
        ind.append(i)
print('ok')