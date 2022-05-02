for num in range(1, 1000):
    n = num
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '11' + r
    if int(r, 2) >= 412:
        print(num)
        break
