for i in range(0, 1000):
    n = i
    n = bin(n)[2:]
    n += n[-1]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    n = int(n, 2)
    if n > 160:
        print(i)
        break
