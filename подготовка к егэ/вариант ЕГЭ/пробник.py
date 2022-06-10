for num in range(100000, 0, -1):
    n = num
    r = bin(n)[2:]
    r = r[::-1]
    if r[0] == '0':
        r = '1' + r
    r += bin(n)[2:]
    res = int(r, 2)
    if res <= 6000:
        print(num)
        break