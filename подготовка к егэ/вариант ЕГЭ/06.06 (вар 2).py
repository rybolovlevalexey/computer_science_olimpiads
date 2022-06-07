file = open('107_17.txt', 'r')
sp = list(map(int, file.read().strip().split()))
k = min(filter(lambda x: x % 21 == 0, sp))
cnt = 0
mxsm = 0

for i in range(len(sp) - 1):
    if sp[i] % k == 0 or sp[i + 1] % k == 0:
        cnt += 1
        if mxsm < sp[i] + sp[i + 1]:
            mxsm = sp[i] + sp[i + 1]
print(cnt, mxsm)
