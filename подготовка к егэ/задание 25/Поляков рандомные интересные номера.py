for num in range(300, 350 + 1):
    sp = [1]
    for d in range(2, num // 2 + 1):
        if num % d == 0:
            sp.append(d)
    sums = sp[0]