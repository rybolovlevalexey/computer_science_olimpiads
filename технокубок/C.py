t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    sp = sorted(map(int, input().split()))
    if k == 1:
        print(sum(sp[:-1]) * 2 + sp[-1])
    else:
        dlina = 0
        