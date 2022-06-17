for num in range(95632, 95650 + 1):
    sp = set()
    sp.add(1)
    x = num
    while x % 2 == 0:
        x //= 2
    sp.add(x)
    for d in range(3, int(x**0.5) + 1, 2):
        if x % d == 0:
            sp.add(d)
            sp.add(x // d)
        if len(sp) > 6:
            break
    if len(sp) == 6:
        print(sorted(sp))