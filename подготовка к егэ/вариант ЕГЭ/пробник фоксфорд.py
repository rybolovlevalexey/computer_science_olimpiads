def f(n):
    if n == 1 or n == 2 or n == 3:
        return n
    elif n % 3 == 0 and n > 3:
        return n + f(n - 1) + f(n - 2) + 3
    elif n > 3 and n % 3 != 0:
        return 1 + f(n - 2) + f(n - 1) + n


print(f(13))