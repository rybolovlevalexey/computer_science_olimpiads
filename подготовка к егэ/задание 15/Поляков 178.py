for a in range(1, 10000):
    flag = True
    for x in range(1, 1000000):
        if (x & 19 == 0) and (x & 38 != 0) or ((x & 43 != 0) or (x & a == 0) and (x & 43 == 0)):
            pass
        else:
            flag = False
            break
    if flag:
        print(a)
        break
