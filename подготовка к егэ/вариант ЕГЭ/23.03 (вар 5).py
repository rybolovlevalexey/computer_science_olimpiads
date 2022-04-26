file = open('17 (4).txt')
sp = file.read().strip().split('\n')
sp = list(map(int, sp))
cnt = 0
mxsm = 0
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if (sp[i] + sp[j]) % 2 != 0 and (sp[i] * sp[j]) % 5 == 0:
            cnt += 1
            if (sp[i] + sp[j]) > mxsm:
                mxsm = (sp[i] + sp[j])
print(cnt, mxsm)
