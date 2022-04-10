sp = list()
for i in range(1529, 9482 + 1):
    if i % 2 == 1 and i // 2 % 2 == 0 and i % 5 == 3:
        sp.append(i)
print(min(sp), sum(sp))
