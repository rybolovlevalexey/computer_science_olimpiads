for x in range(201, 10000):
    l = 2 * x - 15
    m = 2 * x + 30
    while l != m:
        if l > m:
            l = l - m
        else:
            m = m - l
    if m == 45:
        print(x)
        break