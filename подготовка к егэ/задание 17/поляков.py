ans = list()
for x in range(1000, 70000 + 1):
    d1 = 0
    num = x
    while num > 0:
        num //= 8
        d1 += 1
    if d1 != 5:
        continue
    d2 = 0
    num = x
    while num > 0:
        num //= 5
        d2 += 1
    if d2 != 6:
        continue
    if x % 16 == 10 and x // 16 % 16 == 15:
        ans.append(x)
print(len(ans), max(ans))