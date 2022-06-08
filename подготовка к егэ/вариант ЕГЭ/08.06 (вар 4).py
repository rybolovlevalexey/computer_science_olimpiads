file = open('17 (9).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = 0
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if sp[i] % 160 != sp[j] % 160 and (sp[i] % 7 == 0 or sp[j] % 7 == 0):
            cnt += 1
            if sp[i] + sp[j] > mxsm:
                mxsm = sp[i] + sp[j]
print(cnt, mxsm)