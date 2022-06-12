num = 452021 + 1
k = 0
while k < 5:
    m = set()
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            m.add(d)
            m.add(num // d)
        if len(m) >= 3:
            break
    if len(m) >= 2:
        m = min(m) + max(m)
        if m % 7 == 3:
            print(num, m)
            k += 1
    num += 1
