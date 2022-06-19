for num in range(100000):
    x = num
    a = 0
    b = 1
    while x > 0:
        a += 1
        b = b * (x % 1000)
        x = x // 1000
    if a == 2 and b == 11:
        print(num)
        break