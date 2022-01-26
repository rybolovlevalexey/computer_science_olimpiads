for i in range(10000, 0, -1):
    w = i
    w -= 2
    n = 1
    while w < 120:
        w += 7
        n = n * 2 + 2
    if n == 94:
        print(i)

