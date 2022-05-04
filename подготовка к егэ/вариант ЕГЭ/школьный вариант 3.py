for num in range(3, 10000):
    n = num
    r = bin(n)[2:]
    r = r + r[1] + r[0]
    r = int(r, 2)
    if 90 < r:
        print(num)
        break