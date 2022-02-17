for a in range(1000, 1, -1):
    flag = True
    for x in range(1, 20000):
        if not ((x & a == 0) or (x & 69 != 4) or (x & 118 == 6)):
            flag = False
            break
    if flag:
        print(a)
        break
