n = int(input())
sp1 = list()
sp2 = list()
for i in range(n):
    sp1.append(list(map(int, input().split())))
for i in range(n):
    sp2.append(list(map(int, input().split())))
res = list()
for i in range(n):
    res.append(['*'] * n)
flag = True
for i in range(n):
    for j in range(n):
        su = 0
        for k in range(n):
            su += (sp1[i][k] * sp2[k][j])
            if flag:
                print(sp1[i][k], sp2[k][j], su)
        flag = False
        res[i][j] = su
        print(res[i][j])
        su = 0
print(*res, sep='\n')