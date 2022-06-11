sp = list()
def f(n):
    if n > 0:
        f(n - 3)
        sp.append(n)
        f(n // 3)

f(9)
print(''.join(map(str, sp)))