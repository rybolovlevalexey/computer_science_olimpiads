k = 0
num = 500000000 + 1
while k < 5:
    sp = list()
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            sp.append(d)
            sp.append(num // d)
        if len(sp) >= 6:
            break
    if len(sp) >= 3:
        sp = sorted(sp)
        s = sp[-1] + sp[-2] + sp[-3]
        if sum(map(int, list(str(s)))) == 33:
            print(s, max(sp))
            k += 1
    num += 1
