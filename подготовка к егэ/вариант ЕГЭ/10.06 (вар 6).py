cnt = 0
mxsm = 0
file = open('17 (11).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if abs(sp[i] - sp[j]) % 2 == 0 and (sp[i] % 31 == 0 or sp[j] % 31 == 0):
            cnt += 1
            if sp[i] + sp[j] > mxsm:
                mxsm = sp[i] + sp[j]
print(cnt, mxsm)
