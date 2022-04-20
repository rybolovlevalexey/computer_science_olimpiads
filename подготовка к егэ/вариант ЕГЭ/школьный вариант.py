for num in range(1000):
    n = num
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    if r.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    r = int(r, 2)
    if r > 96:
        print(num)
        break
