def f(n):
    if n < 14:
        return 3*n + 2*n + 1
    elif n > 13 and n % 3 == 0:
        return f(n - 1) + 4*n - 3
    else:
        return f(n - 2) + 3*n + 6


ans = 0
for num in range(1, 1000 + 1):
    res = f(num)
    if len(list(filter(lambda x: x % 2 == 1, map(int, list(str(res)))))) == len(str(res)):
        ans += 1
print(ans)