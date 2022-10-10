sp1 = list()
sp2 = list()
res = list()
n, m = map(int, input().split())
for i in range(n):
    sp1.append(list(map(int, input().split())))
input()
m, k = map(int, input().split())
for i in range(m):
    sp2.append(list(map(int, input().split())))
for i in range(max(m, n, k)):
    res.append(['*'] * max(m, n, k))
for i in range(max(n, m)):
    for j in range(max(m, k)):
        su = 0
        for k in range(max(m, k, n)):
            su += (sp1[i][k] * sp2[k][j])
        res[i][j] = su
print(*res, sep='\n')