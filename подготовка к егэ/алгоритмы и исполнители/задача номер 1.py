ans = 0
for i in range(2, 1000):
    n = i
    if n % 4 == 0:
        n //= 2
    else:
        n -= 1
    if n % 5 == 0:
        n //= 5
    else:
        n -= 1
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1

    if n == 3:
        ans += 1
print(ans)