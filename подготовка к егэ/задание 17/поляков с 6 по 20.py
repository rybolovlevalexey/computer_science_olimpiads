sp = list()
for i in range(1156, 12209 + 1):
    if (i % 2 == 0 or i % 5 == 0) and i % 7 != 0 and i % 17 != 0 and i % 13 != 0 and i % 23 != 0:
        sp.append(i)
print(len(sp), max(sp))
