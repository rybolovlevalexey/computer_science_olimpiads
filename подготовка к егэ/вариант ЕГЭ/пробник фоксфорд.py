for a in range(10000, 1, -1):
    flag = True
    for x in range(1, 10000):
        if x % a == 0 or not x % 16 == 0 or not x % 24 == 0:
            pass
        else:
            flag = False
            break
    if flag:
        print(a)
        break
