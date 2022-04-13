sp = list()
for num in range(126849, 126871 + 1):
    delit = list()
    for d in range(2, num // 2 + 2):
        if num % d == 0:
            delit.append(d)
        if len(delit) >= 3:
            break
    if len(delit) >= 3:
        continue
    elif len(delit) == 2:
        delit = [1] + delit + [num]
        sp.append(delit)
print(*sp, sep='\n')