n = int(input())
sp = list(list(map(int, input().split())) for _ in range(n))
flag = True
for i in range(n):
    for j in range(n - i):
        if i == n - 1 - j:
            continue
        if int(sp[i][j]) == int(sp[n - j - 1][n - i - 1]):
            continue
        flag = False
print('YES' if flag else 'NO')