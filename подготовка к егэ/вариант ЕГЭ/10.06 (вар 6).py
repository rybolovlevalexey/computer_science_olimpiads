ans = list()
for a in range(-100, 100):
    flag = True
    for x in range(1000):
        for y in range(1000):
            res = (x >= a or x**2 < 81) and (y**2 > 36 or y <= a)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        ans.append(a)
print(ans)
print(len(ans))