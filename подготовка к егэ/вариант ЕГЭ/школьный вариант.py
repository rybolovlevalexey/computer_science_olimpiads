file = open('zadanie_17.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = 0
for i in range(len(sp) - 1):
    if sp[i] % 16 == 14 or sp[i + 1] == 14:
        cnt += 1
        if sp[i] + sp[i + 1] > mxsm:
            mxsm = sp[i] + sp[i + 1]
print(cnt, mxsm)
