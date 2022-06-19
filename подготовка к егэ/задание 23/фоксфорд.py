for num in range(201, 1000):
    x = num
    L = 2 * x - 15
    M = 2 * x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 45:
        print(num)
        break