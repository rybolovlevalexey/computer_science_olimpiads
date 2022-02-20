for a in range(500000, 1, -1):
    flag = True
    for x in range(1, 1000000):
        if (x % a == 0) or (x % 21 != 0) or (x % 14 == 0):
            pass
        else:
            flag = False
            break
    if flag:
        print(a)
        break
