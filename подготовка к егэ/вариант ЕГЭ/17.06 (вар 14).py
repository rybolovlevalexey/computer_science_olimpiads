file = open('17 (18).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = 0
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if (sp[i] + sp[j]) % 60 == 0 and (sp[i] % 40 == 0 or sp[j] % 40 == 0):
            cnt += 1
            if mxsm < sp[i] + sp[j]:
                mxsm = sp[i] + sp[j]

print(cnt, mxsm)