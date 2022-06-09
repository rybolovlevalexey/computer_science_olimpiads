ansd = dict()
for num in range(174457, 174505 + 1):
    sp = set()
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            sp.add(num // d)
            sp.add(d)
        if len(sp) > 3:
            break
    if len(sp) == 2:
        ansd[num] = sorted(sp)
proizkeyd = dict()
for key, value in ansd.items():
    proizkeyd[value[0] * value[1]] = value
for key in sorted(proizkeyd.keys()):
    print(proizkeyd[key])
