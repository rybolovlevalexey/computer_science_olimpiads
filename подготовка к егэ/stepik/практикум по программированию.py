n, m = map(int, input().split())
sp = list()
for i in range(n):
    line = list("*" for j in range(m))
    sp.append(line)
for j in range(m):
    if j == 0:
        k = 1
    else:
        k = sp[0][j - 1] + 1
    for i in range(n):
        k = k % max(m, n)
        sp[i][j] = k
        k += 1
for i in range(n):
    for j in range(m):
        if sp[i][j] == 0:
            sp[i][j] = max(m, n)
for elem in sp:
    print(*elem)