file = open('17 (13).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
chet = list(filter(lambda x: x % 2 == 0, sp))
sr = sum(chet) / len(chet)
mxsm = 0
for i in range(len(sp) - 1):
    if (sp[i] % 3 == 0 or sp[i + 1] % 3 == 0) and (sp[i] < sr or sp[i + 1] < sr):
        cnt += 1
        if mxsm < sp[i] + sp[i + 1]:
            mxsm = sp[i] + sp[i + 1]
print(cnt, mxsm)
