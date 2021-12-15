for r in range(10, 50 + 1):
    flag = True
    for a in range(1, 10000):
        for x in range(1, 10000):
            if x & 54 != 0 and x & 45 != 0 or x & a == 0 or x & r == 0:
                pass
            else:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(r)
        break
