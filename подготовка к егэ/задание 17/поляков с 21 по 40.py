sp = list()
for i in range(1871, 9197 + 1):
    n1 = 0
    i1 = i
    while i1 > 0:
        n1 += 1
        i1 //= 16
    if n1 != len(str(i)) and i % 9 in [2, 4]:
        sp.append(i)

print(len(sp), min(sp))