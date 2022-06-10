def convert(x, system):
    res = ''
    while x > 0:
        res += str(x % system)
        x //= system
    return res[::-1]


sp = list()
for num in range(1, 96):
    if len(convert(num, 3)) >= 2 and convert(num, 3)[-1] == '1' and convert(num, 3)[-2] == '2' and convert(num, 5)[0] == '3':
        sp.append(num)
print(sp)
print(sum(sp))
