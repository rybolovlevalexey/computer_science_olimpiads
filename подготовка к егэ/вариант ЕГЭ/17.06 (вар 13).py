sp = list()
def f(n):
    if n > 0:
        sp.append(n)
        f(n // 2)
        f(n - 4)

f(9)
print(''.join(map(str, sp)))