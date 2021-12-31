def five_delit(number):
    count = 0
    sp = list()
    for d in range(1, number // 2 + 1):
        if number % d == 0:
            count += 1
            sp.append(d)
        if count > 6:
            return False
    if count == 5:
        return sp


for elem in range(904528, 997438 + 1):
    res = five_delit(elem)
    if res:
        print(res)