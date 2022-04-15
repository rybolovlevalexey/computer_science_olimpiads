for num in range(102714, 102725 + 1):
    sp = list()
    for d in range(2, num // 2 + 1):
        if num % d == 0:
            sp.append(d)
        if len(sp) >= 3:
            break

    if len(sp) == 2:
        sp = [1] + sp + [num]
        print(sp)
