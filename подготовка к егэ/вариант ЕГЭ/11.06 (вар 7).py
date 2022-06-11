for a in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            res = (y + 2*x != 48) or (a < x) or (a < y)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
