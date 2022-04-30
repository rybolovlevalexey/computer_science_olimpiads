file = open('17 (5).txt', 'r')
sp = file.read().strip().split('\n')
sp = list(map(int, sp))
cnt = 0
mxsm = 0

for i in range(len(sp)):
    for j in range(i + 1, len(sp)):
        if (sp[i] + sp[j]) % 10 == 0:
            cnt += 1
            if sp[i] + sp[j] > mxsm:
                mxsm = sp[i] + sp[j]
print(cnt, mxsm)