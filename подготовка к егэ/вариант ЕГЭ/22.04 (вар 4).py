cnt = 0
for a in range(-100, 100):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((x >= 5 or x**2 < a) and (y**2 > a or y <= 5)):
                flag = False
                break
        if not flag:
            break
    if flag:
        cnt += 1
        print(a)
print()
print(cnt)