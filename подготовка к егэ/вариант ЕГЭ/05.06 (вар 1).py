file = open('17 (8).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
chet = list(filter(lambda x: x % 2 == 0, sp))
sr = sum(chet) / len(chet)
mxsm = 0

for i in range(len(sp) - 1):
    i1 = sp[i]
    i2 = sp[i + 1]
    if (i1 % 3 == 0 or i2 % 3 == 0) and (i1 < sr or i2 < sr):
        cnt += 1
        if i1 + i2 > mxsm:
            mxsm = i1 + i2
print(cnt, mxsm)