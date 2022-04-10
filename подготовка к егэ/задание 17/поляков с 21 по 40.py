sp = list()
for i in range(2568, 7858 + 1):
    if (i % 4 == 0 or i % 5 == 0) and i % 11 != 0 and i % 20 != 0 and i % 27 != 0:
        sp.append(i)
print(min(sp), max(sp))