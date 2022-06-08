ans = set()
for num in range(100, 3000 + 1):
    n = num
    r = bin(n)[2:]
    r = r[1:]
    while len(r) > 0 and r[0] == '0':
        r = r[1:]
    if len(r) == 0:
        r = 0
    else:
        r = int(r, 2)
    res = n - r
    ans.add(res)
print(ans)
print(len(ans))
