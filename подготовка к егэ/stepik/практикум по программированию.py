n = int(input())
sp = list()
ans = list()
for i in range(n):
    line = list(map(int, input().split()))
    sp.append(line)
    line = list('*' for j in range(n))
    ans.append(line)
#for d in range(n // 2):
#    for i in range(d, n - d):
#        ans[i][n - 1 - d] = sp[0 + d][i]
#        ans[i][d] = sp[n - 1 - d][i]
#if n % 2 == 1:
#    ans[n // 2][n // 2] = sp[n // 2][n // 2]
for d in range(n // 2):
    for i in range(1 + d, n - 1 - d):
        ans[n - 1 - d][n - i - 1] = sp[i][n - 1 - d]

print(*ans, sep='\n')