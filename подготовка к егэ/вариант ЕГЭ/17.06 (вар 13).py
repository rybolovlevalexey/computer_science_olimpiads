ans = list()
for a in range(-100, 1000):
    flag = True
    for x in range(10000):
        res = (x & 51 == 0) or (x & 41 != 0 or x & a == 0)
        if not res:
            flag = False
    if flag:
        ans.append(a)
        print(a)
print(ans)
