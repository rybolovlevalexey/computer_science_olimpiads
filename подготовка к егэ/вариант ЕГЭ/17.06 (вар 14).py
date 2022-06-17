for num in range(101, 1000):
    x = num
    L = x - 30
    M = x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 30:
        print(num)
        break