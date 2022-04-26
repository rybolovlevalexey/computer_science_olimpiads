p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
a = list()
for num in range(1, 1000):
    flag = True
    for x in range(0, 10000):
        if (not x == num or x in p) and (not x in q or x != num):
            pass
        else:
            flag = False
            break
    if flag:
        a.append(num)
    print(a)
print(len(a))