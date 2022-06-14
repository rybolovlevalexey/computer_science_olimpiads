file = open('17 (16).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = None
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if (sp[i] + sp[j]) % 7 == 0:
            cnt += 1
            if mxsm is None or mxsm < sp[i] + sp[j]:
                mxsm = sp[i] + sp[j]
print(cnt, mxsm)