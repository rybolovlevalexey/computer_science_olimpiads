for i in range(10000):
    x = i
    a = 0
    b = 1
    m = x % 7
    while x > 0:
        d = x % 7
        if d > m:
            a = a + d
        else:
            b = b * d
        x //= 7
    if a == 7 and b == 4:
        print(i)
