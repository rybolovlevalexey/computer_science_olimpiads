sp = list()
for i in range(3672, 9117 + 1):
    if i % 3 == 2 and i % 5 == 4:
        sp.append(i)
print(len(sp), sum(sp))
