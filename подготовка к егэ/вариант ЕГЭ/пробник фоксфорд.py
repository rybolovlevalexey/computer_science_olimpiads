for num in range(1, 1000):
    n = num
    r = bin(n)[2:]
    if n % 2 != 0:
        r += '11'
    else:
        r += '00'
    r += str(sum(map(int, list(r))) % 2)
    r = int(r, 2)
    if r > 177:
        print(r)
        break