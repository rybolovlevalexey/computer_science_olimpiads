for a in range(1, 10000):
    flag = True
    for x in range(1, 100000):
        if (x % 84 == 0) and (x % 90 == 0) or (x % a != 0):
            pass
        else:
            flag = False
    if flag:
        print(a)
        break