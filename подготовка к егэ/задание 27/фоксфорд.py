def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 5 == 0:
        return n // 5 + f(n // 5)
    if n > 0 and n % 5 > 0:
        return (n % 5) + f(n - 1)

for num in range(10000):
    if f(num) == 2021:
        print(num)
        break
