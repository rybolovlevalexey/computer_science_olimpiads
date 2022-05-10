for a in range(1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            res = (x > 9 or x**2 <= a) and (y**2 > a or y <= 9)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
