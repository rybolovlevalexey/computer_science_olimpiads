sp = list()

def f(n):
    if n > 0:
        sp.append('*')
        f(n - 1)
        f(n // 3)

f(6)
print(len(sp))