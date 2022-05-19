for a in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        res = (a % 35 == 0) and ((730 % x != 0) or (a % x == 0) or (110 % x != 0))
        if not res:
            flag = False
            break
    if flag:
        print(a)
        break
