sp = list()
for i in range(1305, 14063 + 1):
    if (i % 2 == 0 or i % 3 == 0) and i % 7 != 0 and i % 17 != 0 and i % 11 != 0 and i % 23 != 0:
        sp.append(i)
print(len(sp), max(sp))
