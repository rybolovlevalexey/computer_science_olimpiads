for num in range(1000000, 2000000 + 1):
    sp = set()
    for d in range(1, int(num**0.5)+1):
        if num % d == 0:
            d2 = num // d
            delta = abs(d2 - d)
            if delta <= 100:
                sp.add(delta)
        if len(sp) >= 3:
            break
    if len(sp) == 3:
        print(num)