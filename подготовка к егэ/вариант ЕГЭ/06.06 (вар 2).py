ans = set()
for number in range(10, 1000 + 1):
    n = number
    r = bin(n)[2:]
    r = r[1:]
    while len(r) > 0 and r[0] == '0':
        r = r[1:]
    if len(r) > 0:
        res = int(r, 2)
    else:
        res = 0
    res = n - res
    ans.add(res)
print(len(ans))
print(ans)