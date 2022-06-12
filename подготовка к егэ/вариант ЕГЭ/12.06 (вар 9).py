sp = list()
def f(n):
    if n > 0:
        f(n - 1)
        sp.append(str(n))
        f(n - 2)

f(4)
print(''.join(sp))