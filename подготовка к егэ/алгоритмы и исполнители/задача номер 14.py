def f(n):
    if n == 30:
        return 8713233
    elif n == 31:
        return 14098309
    elif n == 32:
        return 22811545
    elif n >= 1:
        return (1 + 1 + f(n - 1) + f(n - 2) + 1)
    else:
        return 1


print(f(35))