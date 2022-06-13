def deliteli(x):
    sp = set()
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            sp.add(d)
            sp.add(x // d)
    return sp


for num in range(312614, 312651 + 1):
    res = deliteli(num)
    if len(res) == 6:
        print(sorted(res))