sp = list()

def f(n):
    sp.append(n)
    if n < 5:
        f(n + 1)
        f(n + 3)

f(1)
print(sp)
print(sum(sp))