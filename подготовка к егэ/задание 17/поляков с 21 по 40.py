sp = list()
for i in range(3394, 8599 + 1):
    if i % 3 == 1 and i % 7 == 5:
        sp.append(i)
print(max(sp), sum(sp))
