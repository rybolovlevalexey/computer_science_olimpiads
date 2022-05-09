for num in range(1000000, 0, -1):
    w = num
    n = 1
    while w < 120:
        w += 15
        n = n * 2 + 2
    if n == 94:
        print(num)
        break