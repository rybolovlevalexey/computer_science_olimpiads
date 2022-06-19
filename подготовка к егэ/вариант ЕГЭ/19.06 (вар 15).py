for num in range(12, 14 + 1):
    sp = set()
    sp.add(1)
    sp.add(num)
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            sp.add(d)
            sp.add(num // d)
        if len(sp) >= 5:
            break
    if len(sp) == 4:
        print(sorted(sp))