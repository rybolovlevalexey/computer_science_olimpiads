for i in range(100000):
    x = i
    a = 0
    b = 0
    m = x % 9
    while x > 0:
        d = x % 9
        if d > m:
            a = a + x % 9
        else:
            b = b + 1
        x = x // 9
    if a == 2 and b == 3:
        print(i)