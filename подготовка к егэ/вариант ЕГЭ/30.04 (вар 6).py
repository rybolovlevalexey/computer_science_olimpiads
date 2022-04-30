sp = list()
def f(n):
    sp.append(n)
    if n > 2:
        f(n - 3)
        f(n - 2)
        f(n - 1)

f(4)
print(sp)