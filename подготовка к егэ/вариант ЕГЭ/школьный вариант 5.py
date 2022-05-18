for num in range(1000):
    s = num
    n = 0
    while s * s < 101:
        s += 1
        n += 2
    if n == 10:
        print(num)
        break
