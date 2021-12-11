def f(n):
    if n < 2:
        return 1
    elif n > 1 and n % 2 == 0:
        return 2 * f(n - 1)
    elif n > 1 and n % 2 != 0:
        return 4 * n + f(n - 2)


print(f(45))