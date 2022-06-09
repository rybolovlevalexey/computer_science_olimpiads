file = open('17 (10).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = 0
for i in range(len(sp) - 1):
    if sp[i] % 3 == 0 or sp[i + 1] % 3 == 0:
        cnt += 1
        if sp[i] + sp[i + 1] > mxsm:
            mxsm = sp[i] + sp[i + 1]
print(cnt, mxsm)