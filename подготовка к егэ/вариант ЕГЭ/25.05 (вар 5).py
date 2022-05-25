for a in range(0, 1000):
    flag = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            res = (x*y < a) or (y > x) or (x >= 8)
            if not res:
                flag = False
                break
            if y > x:
                break
        if not flag:
            break
    if flag:
        print(a)
        break