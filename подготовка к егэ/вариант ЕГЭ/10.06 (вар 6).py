for num in range(1000):
    n = num
    r = bin(n)[2:]
    s = sum(map(int, list(r)))
    r += str(s % 2)
    s = sum(map(int, list(r)))
    r += str(s % 2)
    res = int(r, 2)
    if res > 43:
        print(res)
        break