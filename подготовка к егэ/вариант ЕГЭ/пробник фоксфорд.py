for n in range(1000):
    r = bin(n)[2:]
    if n % 2 != 0:
        r += '10'
    else:
        r += '01'
    s = sum(map(int, list(r))) % 2
    r += str(s)
    r = int(r, 2)
    if r > 147:
        print(r)
        break