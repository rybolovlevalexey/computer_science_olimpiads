n = int(input())
sp = list()
mx = 0
flag = True
for i in range(n):
    line = list(map(int, input().split()))
    sp.append(line)
for i in range(n):
    if i <= n // 2:
        line = list(sp[i][:i+1] + sp[i][n-1-i:])
    else:
        line = list(sp[i][:n-i] + sp[i][i:])
    for elem in line:
        if flag or elem > mx:
            mx = elem
            flag = False
print(mx)