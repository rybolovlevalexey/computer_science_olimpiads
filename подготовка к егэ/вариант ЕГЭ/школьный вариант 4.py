for num in range(-1000, 1000):
    x = num
    L = 0
    M = 0
    while x > 0:
        L += 1
        if x % 2 == 1:
            M = M + (x % 10)
        x = x // 10
    if L == 3 and M == 8:
        print(num)
        break