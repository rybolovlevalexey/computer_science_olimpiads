for a in range(100, -100, -1):
    flag = True
    for x in range(500):
        for y in range(500):
            if (x > 3 or x**2 <= a) and (y**2 > a or y <= 3):
                pass
            else:
                flag = False
    if flag:
        print(a)
        break