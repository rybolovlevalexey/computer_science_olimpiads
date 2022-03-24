def f(n):
    if n > 3:
        return f(n - 2) + f(n // 2)
    else:
        return n


print(f(9))