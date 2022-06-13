for num in range(1000):
    n = num
    r = bin(n)[2:]
    sp = sum(map(int, list(r)))
    if sp % 2 == 0:
        r += '00'
    else:
        r += '11'
    res = int(r, 2)
    if res > 114:
        print(res, num)
