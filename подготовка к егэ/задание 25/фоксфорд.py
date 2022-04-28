for num in range(247264322, 369757523 + 1):
    sp = list()
    for d1 in range(2, int(num **0.5) + 1):
        if num % d1 == 0:
            sp.append(d1)
            #for d2 in range(2, int(num))
    if len(sp) == 3:
        print(num, max(sp))
