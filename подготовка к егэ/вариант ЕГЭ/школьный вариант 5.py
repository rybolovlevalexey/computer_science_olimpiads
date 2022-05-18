cnt = 0
for num in range(2, 1000):
    n = num
    r = bin(n)[2:]
    summa = sum(map(int, list(r)))
    r += str(summa % 2)
    if summa > len(r) - summa - 1:
        r += '0'
    else:
        r += '1'
    r = int(r, 2)
    if 50 <= r <= 80:
        cnt += 1
print(cnt)