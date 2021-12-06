for i in range(1, 1000):
    n = i
    n = bin(n)[2:]
    su = sum(map(int, list(n)))
    n += str(su % 2)
    su = sum(map(int, list(n)))
    n += str(su % 2)
    if int(n, 2) > 63:
        print(int(n, 2))
        break