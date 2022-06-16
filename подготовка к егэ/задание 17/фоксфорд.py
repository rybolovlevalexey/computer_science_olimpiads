file = open('17_7.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = mxsm = 0
sr = sum(sp) / len(sp)
for i in range(len(sp) - 1):
    if abs(sp[i] - sp[i - 1]) <= 20 and sp[i] + sp[i + 1] > sr:
        cnt += 1
        if sp[i] + sp[i + 1] > mxsm:
            mxsm = sp[i] + sp[i + 1]
print(cnt, mxsm)