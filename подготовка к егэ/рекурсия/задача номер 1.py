def f(n):
    if n == 1:
        return 2
    return f(n - 1) + g(n)


def g(n):
    if n == 1:
        return 1
    return f(n - 1) * g(n - 1)


print(f(5))