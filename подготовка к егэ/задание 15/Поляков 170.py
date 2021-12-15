for a in range(1, 10000):
    flag = True
    for x in range(1, 100000):
        if (x & 24 != 0) or (x & a != 0) or (x & 26 == 0) and (x & 13 == 0):
            pass
        else:
            flag = False
            break
    if flag:
        print(a)
        break
