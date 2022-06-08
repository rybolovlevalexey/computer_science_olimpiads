for num in range(0, 256):
    n = num
    r = bin(n)[2:]
    while len(r) < 8:
        r = '0' + r
    r1 = ''
    for elem in r:
        if elem == '0':
            r1 += '1'
        else:
            r1 += '0'
    res = int(r1, 2)
    res = res - n
    if res == 133:
        print(num)
