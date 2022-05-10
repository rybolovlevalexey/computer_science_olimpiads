for num in range(1, 1000):
    n = num
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    if int(r, 2) > 52:
        print(num)
        break