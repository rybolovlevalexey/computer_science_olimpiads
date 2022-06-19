for a in range(100, 200):
    flag = True
    for x in range(10000):
        for y in range(10000):
            res = (2*x + 3*y < a) or (x >= y) or (y > 24)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break