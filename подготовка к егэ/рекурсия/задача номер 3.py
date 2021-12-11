def f(n):
    if n == 1:
        return 1
    elif n == 20:
        return 262144
    elif n == 25:
        return 8388608
    return f(n - 1) - g(n - 1)


def g(n):
    if n == 1:
        return 0
    elif n == 20:
        return -262144
    elif n == 25:
        return -8388608
    elif n == 30:
        return -268435456
    return g(n - 1) - f(n - 1)


print(g(34))