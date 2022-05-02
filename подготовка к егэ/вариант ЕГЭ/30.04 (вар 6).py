for num in range(101000000, 102000000 + 1, 2):
    delit = set()
    delit.add(num)
    for d in range(2, num // 2 + 1, 2):
        if num % d == 0:
            delit.add(d)
        if len(delit) > 4:
            break
    if len(delit) == 3:
        print(num)