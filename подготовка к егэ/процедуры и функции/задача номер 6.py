for i in range(0, 256):
    r = bin(i)[2:]
    r = '0' * (8 - len(r)) + r
    r1 = ''
    for j in r:
        if j == '1':
            r1 += '0'
        else:
            r1 += '1'
    r1 = int(r1, 2)
    res = r1 - i
    if res == 97:
        print(i)
        break