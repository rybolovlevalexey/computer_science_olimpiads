file = open('17 (3).txt', 'r')
cnt = 0
mxsm = 0
sp = file.read().strip().split('\n')
sp = list(map(int, sp))
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if (sp[i] * sp[j]) % 26 == 0:
            cnt += 1
            if (sp[i] + sp[j]) > mxsm:
                mxsm = (sp[i] + sp[j])
print(cnt, mxsm)
