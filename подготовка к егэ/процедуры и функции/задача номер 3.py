def func(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + func(n / 2)
    else:
        return func(n + 1)


for x in range(1, 100):
    if func(x) == 105:
        print(x)
        break