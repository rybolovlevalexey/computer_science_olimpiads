for num in range(-1000, 1000):
    x = num
    a = 0
    b = 10
    while x > 0:
        d = x % 6
        if d > a:
            a = d
        if d < b:
            b = d
        x = x // 6
    res = a + b
    if res == 8:
        print(num)
        break