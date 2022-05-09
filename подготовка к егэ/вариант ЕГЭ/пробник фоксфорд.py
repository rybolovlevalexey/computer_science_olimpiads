for num in range(1000, 9999):
    x = num
    a = 0
    b = 1
    while x > 0:
        if x % 2 == 0:
            a += x % 8
        else:
            b *= x % 8
        x //= 8
    if a == 12 and b == 1:
        print(num)
        break