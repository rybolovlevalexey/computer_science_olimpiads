n, m = map(int, input().split())
sp = [['*'] * m for i in range(n)]
start = 1
for i in range(n):
    num = start
    for j in range(m):
        sp[i][j] = num
        num += 1
        if num > m:
            num = 1
    start += 1
    if start > m:
        start = 1
for elem in sp:
    print(*elem, sep=' ')