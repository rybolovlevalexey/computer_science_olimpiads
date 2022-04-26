for num in range(1, 1000):
    n = num
    r = bin(n)[2:]
    r += str(sum(map(int, list(r))) % 2)
    r += str(sum(map(int, list(r))) % 2)
    r = int(r, 2)
    if r > 97:
        print(num)
        break
