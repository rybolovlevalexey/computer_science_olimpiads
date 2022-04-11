sp = list()
for i in range(3542, 15876 + 1):
    if (i % 2 == 0 or i % 9 == 0) and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
        sp.append(i)
print(len(sp), max(sp))
