for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (x % a == 0) or not (x % 6 == 0) or not (x % 4 == 0):
                pass
            else:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
