sp = list()
for i in range(3905, 7998 + 1):
    if i % 100 // 10 not in [0, 5] and 2 <= i % 1000 // 100 <= 6:
        sp.append(i)
print(len(sp), min(sp))