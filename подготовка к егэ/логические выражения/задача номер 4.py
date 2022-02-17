for a1 in range(-100, 100):
    for a2 in range(100, a1, -1):
        flag = True
        for x in range(-200, 200):
            if not(((not a1 <= x <= a2) or ((x + 18)*(x - 8) <= 0)) and (((x + 14)*(x - 8) > 0) or (a1 <= x <= a2))):
                flag = False
                break
        if flag:
            print(a1, a2)
            break