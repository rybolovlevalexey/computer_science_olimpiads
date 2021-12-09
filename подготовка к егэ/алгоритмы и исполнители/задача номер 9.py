for i in range(10000, 100000):
    x = i
    a = 0
    b = 0
    while x > 0:
        y = x % 10
        if y > 4:
            a = a + 1
        if y < 7:
            b = b + 1
        x = x // 10
    if a == 2 and b == 4:
        print(i)