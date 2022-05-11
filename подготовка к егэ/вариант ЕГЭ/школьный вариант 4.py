for ans in range(10000):
    n = ans
    r = bin(n)[2:]
    if len(r) < 8:
        r = '0' * (8 - len(r)) + r
    num = ''
    for elem in r:
        if elem == '1':
            num += '0'
        else:
            num += '1'
    num = int(num, 2)
    res = num - n
    if res == 113:
        print(ans)
        break