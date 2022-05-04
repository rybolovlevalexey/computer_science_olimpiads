ans = 0
for num in range(1, 100000):
    d = num
    n = 27
    s = 12
    while s <= 2019:
        s += d
        n += 16
    if n == 171:
        ans += 1
        print(num)
    if num % 100 == 0:
        print(num)
print(ans)