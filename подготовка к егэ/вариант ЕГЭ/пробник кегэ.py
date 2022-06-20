for num in range(1000):
    n = num
    res = bin(n)[2:]
    s = sum(map(int, list(res)))
    res += str(s % 2)
    s = sum(map(int, list(res)))
    res += str(s % 2)
    res = int(res, 2)
    if res > 60:
        print(res)
        break