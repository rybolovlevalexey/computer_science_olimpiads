sp = list()

def f(n):
    if n < 8:
        f(n + 3)
        sp.append(n)
        f(2 * n)

f(1)
print(''.join(map(str, sp)))
