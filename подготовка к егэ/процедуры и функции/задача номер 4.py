def g(n):
    if n == 1:
        return 0
    elif n == 20:
        return -262144
    elif n == 21:
        return -524288
    elif n == 23:
        return -2097152
    elif n == 24:
        return -4194304
    elif n == 25:
        return -8388608
    elif n == 26:
        return -16777216
    elif n == 27:
        return -33554432
    elif n == 28:
        return -67108864
    elif n == 29:
        return -134217728
    elif n == 30:
        return -268435456
    elif n == 31:
        return -536870912
    elif n == 32:
        return -1073741824
    elif n > 1:
        return g(n - 1) - f(n - 1)

def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) - g(n - 1)


print(g(34))