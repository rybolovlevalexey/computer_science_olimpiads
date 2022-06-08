d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
def convert(num, syst):
    res = ''
    while num > 0:
        ost = num % syst
        if 10 <= ost <= 15:
            res += d[ost]
        else:
            res += str(num % syst)
        num //= syst
    return res[::-1]


for system in range(2, 100):
    result = convert(87, system)
    if result[-1] == '2' and len(result) <= 2:
        print(system)