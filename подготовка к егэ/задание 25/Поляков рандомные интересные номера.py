num = 2
while num <= 263000:
    s = 1 + num
    for d in range(2, num // 2 + 1):
        if num % d == 0:
            s += d
    su = 1 + s
    for d in range(2, s // 2 + 1):
        if s % d == 0:
            su += d
    if num * 2 == su:
        print(num)
    num *= 2
