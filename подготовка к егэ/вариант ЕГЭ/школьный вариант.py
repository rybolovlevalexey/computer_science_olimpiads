for num in range(-1000, 1000):
    s = num
    n = 105
    while n > s:
        s += 3
        n -= 2
    if n == 67:
        print(num)
        break
