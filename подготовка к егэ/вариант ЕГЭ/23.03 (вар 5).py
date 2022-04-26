for num in range(101, 10000):
    x = num
    L = x
    M = 65
    if L % 2 == 0:
        M = 52
    while M != L:
        if L > M:
            L -= M
        else:
            M -= L
    if M == 26:
        print(num)
        break
