sp = list()
for i in range(3712, 8432 + 1):
    if i % 4 == i % 2 and (i % 13 == 0 or i % 14 == 0 or i % 15 == 0):
        sp.append(i)
print(len(sp), min(sp))
