for a in range(1, 100):
    flag = True
    for x in range(1000):
        for y in range(1000):
            res = (y + 2 * x < a) or (x > 30) or (y > 20)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break
