for a in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            res = (2*x + 3*y > 30) or (x + y <= a)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break