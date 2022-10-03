n, m = map(int, input().split())
for i in range(n):
    sp = list()
    if i % 2 == 0:
        dot = 1
    else:
        dot = -1
    for j in range(m):
        if dot == 1:
            sp.append(".")
        else:
            sp.append("*")
        dot *= -1
    print(*sp)
