def f(n):
    if n < 4:
        return n - 1
    elif n >= 4 and n % 3 == 0:
        return n + 2*f(n - 1)
    elif n >= 4 and n % 3 != 0:
        return f(n - 2) + f(n - 3)

res = f(25)
print(res)
print(sum(list(map(int, list(str(res))))))