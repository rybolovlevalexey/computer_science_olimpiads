file = open('17 (20).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = None
for i in range(len(sp) - 1):
    if abs(sp[i]) % 5 == 0 and abs(sp[i + 1]) % 5 == 0 and abs(sp[i]) % 3 != 0 and abs(sp[i + 1]) % 3 != 0:
        cnt += 1
        if sp[i] + sp[i + 1] > 0 and (mxsm is None or sp[i] + sp[i + 1] < mxsm):
            mxsm = sp[i] + sp[i + 1]
print(cnt, mxsm)