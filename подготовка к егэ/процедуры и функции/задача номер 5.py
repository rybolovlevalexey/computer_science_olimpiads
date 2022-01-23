for n in range(1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '01'
    else:
        r += '10'
    r = int(r, 2)
    if r > 73:
        print(n)
        break
