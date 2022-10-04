n = int(input())
sp = list(['*'] * n for i in range(n))
for i in range(n):
    st = input().split()
    for j in range(n):
        sp[j][i] = st[j]
for elem in sp:
    print(*elem, sep=' ')