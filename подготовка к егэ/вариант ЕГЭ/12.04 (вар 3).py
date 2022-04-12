sp = list()

def f(n):
    if n > 0:
        g(n - 1)


def g(n):
    sp.append('*')
    if n > 1:
        f(n - 2)

f(11)
print(sp)