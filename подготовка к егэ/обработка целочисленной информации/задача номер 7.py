def func(number):
    sp = list()
    for d in range(1, number // 2 + 1):
        if number % d == 0:
            sp.append(d)
    if len(sp) == 5:
        sp = [number] + sp + [number]
        return sp
    return False


for elem in range(164700, 164752 + 1):
    res = func(elem)
    if res:
        print(res)