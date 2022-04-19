sp = list()
for num in range(1000000):
    a = 0
    b = 0
    x = num
    while x > 0:
        d = x % 10
        if d > 4:
            a += 1
        if d < 7:
            b += 1
        x = x // 10
    if a == 2 and b == 3:
        sp.append(num)
print(max(sp))
