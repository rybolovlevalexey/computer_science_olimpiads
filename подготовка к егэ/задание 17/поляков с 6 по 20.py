sp = list()
for i in range(1390, 12567 + 1):
    if (i % 3 == 0 or i % 5 == 0) and i % 11 != 0 and i % 13 != 0 and i % 7 != 0 and i % 23 != 0:
        sp.append(i)
print(len(sp), max(sp))
