for num in range(10000):
    x = num
    a = 0
    b = 1
    while x > 0:
        if x % 2 == 0:
            a += x % 7
        else:
            b *= x % 7
        x //= 7
    if a == 4 and b == 9:
        print(num)
        break