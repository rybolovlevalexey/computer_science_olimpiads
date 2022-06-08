output = 0
num = 10000000 + 1
while output < 5:
    sp = set()
    s = 0
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            sp.add(d)
            sp.add(num // d)
        if len(sp) >= 3:
            break
    if len(sp) >= 2:
        s = sorted(sp)[-1] + sorted(sp)[-2]
    if 0 < s < 10000:
        print(s)
        output += 1
    num += 1
