for num in range(1000, 20000 + 1):
    sp = list()
    for d in range(1, num // 2 + 2):
        if num % d == 0:
            sp.append(d)
    if num - sum(sp) == 1:
        print(num)
