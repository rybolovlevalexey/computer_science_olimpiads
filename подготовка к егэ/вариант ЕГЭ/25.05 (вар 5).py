file = open('17 (7).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = 0

for i in range(len(sp)):
    for j in range(i + 1, len(sp)):
        if (sp[i] + sp[j]) % 80 == 0 and (sp[i] % 50 == 0 or sp[j] % 50 == 0):
            cnt += 1
            if sp[i] + sp[j] > mxsm:
                mxsm = sp[i] + sp[j]
print(cnt, mxsm)
