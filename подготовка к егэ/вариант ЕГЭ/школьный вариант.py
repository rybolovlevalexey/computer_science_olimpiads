for num in range(190061, 190080 + 1):
    delit = set()
    delit.add(1)
    if num % 2 != 0:
        delit.add(num)
    for d in range(3, num // 2 + 1, 2):
        if num % d == 0:
            delit.add(d)
        if len(delit) > 5:
            break
    if len(delit) == 4:
        print(num, delit)