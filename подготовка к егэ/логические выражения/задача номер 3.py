for a in range(-500, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if not (((y - 40 < a) and (30 - y < a)) or (x * y > 20)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        break
