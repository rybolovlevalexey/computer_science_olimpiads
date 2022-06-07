num = 452021 + 1
anscnt = 0
while anscnt < 5:
    m = 0
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            m += d
            m += (num // d)
            break
    if m % 7 == 3:
        print(num, m)
        anscnt += 1
    num += 1
