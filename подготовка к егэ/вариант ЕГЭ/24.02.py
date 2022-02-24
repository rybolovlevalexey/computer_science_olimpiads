for a in range(1000, 0, -1):
    flag = True
    for x in range(10000):
        for y in range(10000):
            if (2*x + 3*y < 30) or (x + y >= a):
                pass
            else:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break
