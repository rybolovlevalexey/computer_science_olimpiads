n = 0
num = 700001
while n < 3:
    su = 0
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            su += d
            su += (num // d)
    if su > 1000000:
        print(num, su)
        n += 1
    num += 1
