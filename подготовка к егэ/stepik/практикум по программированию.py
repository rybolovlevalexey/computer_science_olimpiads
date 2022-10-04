n = int(input())
sp = list()
for i in range(n):
    if 0 <= i <= 2:
        sp.append(1)
    else:
        sp.append(sp[-1] + sp[-2] + sp[-3])
print(*sp)