for a in range(0, 200):
    flag = True
    for x in range(1, 1000):
        if (x & a != 0) or (x & 60 == 0) or (x & 105 != 0):
            pass
        else:
            flag = False
    if flag:
        print(a)
        break