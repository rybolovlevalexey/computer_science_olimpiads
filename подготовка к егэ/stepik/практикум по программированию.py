x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
sp1 = list()
sp2 = list()
for i in range(y1):
    sp1.append(list(map(int, input().split())))
for i in range(y2):
    sp2.append(list(map(int, input().split())))
res = list()
for i in range(min(y1, y2)):
    res.append(['*'] * min(x1, x2))
flag = True
for i in range(min(y1, y2)):
    for j in range(min(x1, x2)):
        su = 0
        for k in range(max(x1, x2)):
            su += (sp1[i][k] * sp2[k][j])
            if flag:
                print(sp1[i][k], sp2[k][j], su)
        flag = False
        res[i][j] = su
        print(res[i][j])
        su = 0
print(*res, sep='\n')