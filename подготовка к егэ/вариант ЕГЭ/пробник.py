sp = list()
for r in range(1000):
    flag = True
    for x in range(10000):
        for a in range(10000):
            res = (x & 108 != 0 and x & 60 != 0 or x & a == 0) or (x & r == 0)
            if not res:
                flag = False
                break
        if not flag:
            break
    if flag:
        sp.append(r)
print(sp)
print(len(sp))