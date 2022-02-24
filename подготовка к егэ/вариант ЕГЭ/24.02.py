for num in range(10000, 0, -1):
    x = num
    l = 0
    m = 0
    while x > 0:
        l += 1
        if x % 2 != 0:
            m = m + x % 8
        x //= 8
    if l == 3 and m == 6:
        print(num)
        break