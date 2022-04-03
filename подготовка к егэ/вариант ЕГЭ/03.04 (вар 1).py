ans = list()

for a in range(100):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not ((x >= 6 or x**2 < a) and (y**2 > a or y <= 6)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        ans.append(a)
print(len(ans))
