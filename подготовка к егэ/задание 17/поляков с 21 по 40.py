sp = list()
for i in range(3439, 7410 + 1):
    if i % 6 != i % 2 and (i % 9 == 0 or i % 10 == 0 or i % 11 == 0):
        sp.append(i)
print(len(sp), max(sp))
