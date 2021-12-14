for a in range(1, 200):
    flag = True
    for x in range(1, 1000):
        if (x & 13 != 0) and (x & a == 0) or (x & 13 != 0) or (x & a != 0) or (x & 39 == 0):
            pass
        else:
            flag = False
    if flag:
        print(a)
        break