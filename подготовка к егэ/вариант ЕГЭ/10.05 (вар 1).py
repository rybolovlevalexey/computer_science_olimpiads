file = open('17 (6).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
mxsm = 0
for i in range(len(sp) - 2):
    c = max(sp[i], sp[i + 1], sp[i + 2])
    a = min(sp[i], sp[i + 1], sp[i + 2])
    b = sum([sp[i], sp[i + 1], sp[i + 2]]) - a - c
    if c**2 < a**2 + b**2:
        cnt += 1
        if (a + b + c) > mxsm:
            mxsm = a + b + c
print(cnt, mxsm)