sp = list()
for i in range(3232, 8299 + 1):
    if (i % 2 == 0 or i % 7 == 0) and i % 15 != 0 and i % 28 != 0 and i % 41 != 0:
        sp.append(i)

print(min(sp), max(sp))