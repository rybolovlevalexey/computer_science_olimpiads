for num in range(78920, 92430 + 1):
    #if int(num ** 0.5) != num ** 0.5:
    #    continue
    sp = set()
    sp.add(1)
    sp.add(num)
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            sp.add(d)
            sp.add(num // d)

    if len(sp) == 5:
        print(sorted(sp))
