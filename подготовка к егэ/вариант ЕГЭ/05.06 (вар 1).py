for num in range(45000000, 50000000 + 1):
    x = num
    while x % 2 == 0:
        x //= 2
    if int(x ** 0.5) ** 2 != x:
        continue
    sp = set()
    for d in range(3, int(x ** 0.5) + 1, 2):
        if num % d == 0:
            sp.add(d)
            sp.add(x // d)
        if len(sp) >= 4:
            break
    if len(sp) == 3:
        print(num)