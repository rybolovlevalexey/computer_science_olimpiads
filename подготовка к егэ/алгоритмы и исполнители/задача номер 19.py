for num in range(100000, 10000, -1):
    x = num
    a = 0
    b = 0
    while x > 0:
        y = x % 10
        if y > 3:
            a = a + 1
        else:
            b = b - 1
        if y < 8:
            b = b + 1
        x = x // 10
    if a == 2 and b == 1:
        print(num)
        break