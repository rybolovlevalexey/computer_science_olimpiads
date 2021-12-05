for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    if i % 2 == 0:
        n += '01'
    else:
        n += '10'
    if int(n, 2) > 73:
        print(i)
        break
