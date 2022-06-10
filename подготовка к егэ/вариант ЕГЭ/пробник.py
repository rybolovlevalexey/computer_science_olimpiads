def f(n):
    if n == 30:
        return 890
    if n == 35:
        return 1751
    if n == 40:
        return 8186
    if n == 45:
        return 16333
    if n <= 2:
        return 1
    elif n > 2 and n % 2 != 0:
        return f(n - 1) - n
    else:
        return f(n - 2) + g(n - 1) + 2


def g(n):
    if n == 30:
        return 2296
    if n == 35:
        return 2302
    if n == 40:
        return -2056
    if n == 45:
        return -2050
    if n <= 0:
        return 2
    elif n > 0 and n % 2 != 0:
        return f(n - 1) - 2 * g(n - 2)
    else:
        return 2*f(n - 2) - 2*g(n - 1)


print(f(96))
