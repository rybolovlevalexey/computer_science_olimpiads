def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n % 2 == 0 and n > 2:
        return n * f(n - 1) + 2
    elif n % 2 != 0 and n > 2:
        return 1 + f(n - 2) + f(n - 1)

print(f(9))
