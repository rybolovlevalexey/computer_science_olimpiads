sp = list()
for i in range(7747, 25122):
    if (i % 11 == 0 or i % 12 == 0 or i % 17 == 0) and i % 10 == i % 6:
        sp.append(i)
print(len(sp))
print(max(sp))