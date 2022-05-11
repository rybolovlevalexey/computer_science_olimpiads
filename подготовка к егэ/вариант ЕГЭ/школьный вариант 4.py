for a in range(1, 100):
    flag = True
    for x in range(1, 10000):
        res = (x % a != 0) or (x % 28 != 0) or (x % 42 == 0)
        if not res:
            flag = False
            break
    if flag:
        print(a)
        break
