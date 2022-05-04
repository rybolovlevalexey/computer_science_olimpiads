for a in range(0, 1000):
    flag = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            res = (3*x + 5*y < a) or (x >= y) or (y > 8)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break