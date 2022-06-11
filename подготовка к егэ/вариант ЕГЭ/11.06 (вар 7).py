file = open('17 (12).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
sr = sum(filter(lambda x: x % 2 != 0, sp)) / len(list(filter(lambda x: x % 2 != 0, sp)))
cnt = 0
mxsm = 0
for i in range(len(sp) - 1):
    i1 = sp[i]
    i2 = sp[i + 1]
    if (i1 % 5 == 0 or i2 % 5 == 0) and (i1 < sr or i2 < sr):
        cnt += 1
        if mxsm < i1 + i2:
            mxsm = i1 + i2
print(cnt, mxsm)