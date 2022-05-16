ans = list()
pornom = 1

for num in range(248015, 251575 + 1, 2):
    cntd = set()
    midd = 0
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0 and num // d != d:
            cntd.add(num // d)
            cntd.add(d)
        elif d * d == num:
            cntd.add(d)
            midd = d
    if len(cntd) % 2 == 1:
        print(pornom, num, len(cntd), midd)
        pornom += 1
