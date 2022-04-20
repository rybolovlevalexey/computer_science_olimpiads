for a in range(15, 30):
    flag = True
    for x in range(10000):
        for y in range(10000):
            res = (5*x + 3*y != 60) or ((a > x) and (a > y)) and (5*x + 3*y == 60) or ((a > x) and (a > y))
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break
