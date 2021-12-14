sp = list()

for a in range(1, 1001):
    flag = True
    for x in range(1, 200):
        if (a % 12 == 0) and (not 530 % x == 0 or a % x == 0 or not 170 % x == 0):
            pass
        else:
            flag = False
    if flag:
        sp.append(a)
print(sp)
print(len(sp))