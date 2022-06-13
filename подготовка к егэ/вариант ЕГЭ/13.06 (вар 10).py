sp = list()
def f(n):
    if n < 8:
        sp.append(n)
        f(2 * n)
        f(n + 3)
f(1)
print(''.join(map(str, sp)))
