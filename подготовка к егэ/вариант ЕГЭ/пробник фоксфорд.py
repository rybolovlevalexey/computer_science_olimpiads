for a in range(0, 100):
    flag = True
    for x in range(1000):
        for y in range(1000):
            res = (x > 4 or x**2 <= a) and (y**2 > a or y <= 4)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break
