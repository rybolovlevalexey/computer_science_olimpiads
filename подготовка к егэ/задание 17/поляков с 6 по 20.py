sp = list()
for i in range(2320, 10987 + 1):
    if (i % 2 == 0 or i % 7 == 0) and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        sp.append(i)
print(len(sp), max(sp))
