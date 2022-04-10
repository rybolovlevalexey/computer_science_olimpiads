sp = list()
for i in range(2807, 8558 + 1):
    if i % 2 == 1 and i // 2 % 2 == 1 and i % 9 == 5:
        sp.append(i)
print(max(sp), sum(sp))
