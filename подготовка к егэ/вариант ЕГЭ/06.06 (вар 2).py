d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
def five(x):
    res = ''
    while x > 0:
        res += str(x % 5)
        x //= 5
    return res[::-1]
def six(x):
    res = ''
    while x > 0:
        res += str(x % 6)
        x //= 6
    return res[::-1]
def eleven(x):
    res = ''
    while x > 0:
        ost = x % 11
        if ost >= 10:
            res += d[ost]
        else:
            res += str(ost)
        x //= 11
    return res[::-1]

for num in range(1, 10000):
    if len(six(num)) == 2 and len(five(num)) == 3 and eleven(num)[-1] == '1':
        print(num)