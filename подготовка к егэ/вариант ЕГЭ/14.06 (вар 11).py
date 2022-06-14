sp = list()
def f(n):
    if n > 2:
        sp.append(n)
        f(n - 3)
        f(n - 4)
f(10)
print(sp)
print(sum(sp))