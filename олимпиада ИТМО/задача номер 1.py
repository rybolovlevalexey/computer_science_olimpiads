answer = 31323

for m in range(100000, 10000000):
    c = 8
    n = 1
    t = 0
    r = 0
    print(m)
    while m != 0:
        t = 0
        if m >= c:
            t += 1
            m -= c
        else:
            r = r + m * n
            n = n * 10
            m = t
    if r == answer:
        print(m)
        break