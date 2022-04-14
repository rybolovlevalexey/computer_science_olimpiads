num = 500000001
n = 0
while n < 5:
    sp = list()
    for d in range(2, num // 2 + 3):
        if num % d == 0:
            sp.append(d)
        if len(sp) == 5:
            break
    if len(sp) == 5:
        proiz = 1
        for j in sp:
            proiz *= j
        n += 1
        print(proiz)
