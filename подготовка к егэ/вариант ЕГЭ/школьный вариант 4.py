for num in range(100000, 0, -1):
    s = num
    n = 1
    while s < 208:
        s += 20
        n *= 2
    if n == 256:
        print(num)
        break
