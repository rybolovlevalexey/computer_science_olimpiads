for num in range(1000):
    n = num
    r = bin(n)[2:]
    summa = sum(map(int, list(r)))
    r += str(summa % 2)
    summa = sum(map(int, list(r)))
    r += str(summa % 2)
    ans = int(r, 2)
    if ans > 97:
        print(ans)
        break