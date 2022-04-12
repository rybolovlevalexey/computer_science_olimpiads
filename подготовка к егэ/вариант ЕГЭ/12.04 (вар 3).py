for n in range(0, 256):
    x = bin(n)
    x = x[2:]
    while len(x) < 8:
        x = '0' + x
    y = ''
    for elem in x:
        if elem == '0':
            y += '1'
        else:
            y += '0'
    res = int(y, 2)
    if res - n == 111:
        print(n)