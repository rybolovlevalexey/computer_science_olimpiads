for num in range(100000, 0, -1):
    x = num
    L = 0
    M = 0
    while x > 0:
        L += 1
        if x % 2 == 0:
            M = M + (x % 10) // 2
        x = x // 10
    if L == 3 and M == 7:
        print(num)
        break