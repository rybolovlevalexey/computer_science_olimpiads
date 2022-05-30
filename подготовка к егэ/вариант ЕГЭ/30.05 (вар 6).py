ans = 0
an = 0
for num in range(10000):
    n = num
    res = bin(n)[2:]
    if n % 2 == 0:
        res += '10'
    else:
        res += '01'
    res = int(res, 2)
    if res <= 102 and res > ans:
        ans = res
        an = num
print(ans)
print(an)