for num in range(150750, 150764 + 1):
    sp = [1]
    for d in range(2, num // 2 + 1):
        if num % d == 0:
            sp.append(d)
        if len(sp) >= 4:
            break
    sp.append(num)
    if len(sp) == 4:
        print(*sp)
