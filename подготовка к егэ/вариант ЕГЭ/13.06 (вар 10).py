file = open('27991_A.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
mxsm = 0

for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if abs(sp[i] - sp[j]) % 2 == 0 and (sp[i] % 17 == 0 or sp[j] % 17 == 0) and sp[i] + sp[j] > mxsm:
            mxsm = sp[i] + sp[j]
print(mxsm)
