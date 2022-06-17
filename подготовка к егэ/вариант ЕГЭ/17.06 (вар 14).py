for a in range(0, 1000):
    flag = True
    for x in range(1000):
        res = (x & 51 == 0) or (x & 41 != 0) or (x & a == 0)
        if not res:
            flag = False
            break
    if flag:
        print(a)
        break