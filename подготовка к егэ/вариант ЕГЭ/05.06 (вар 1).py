sp = list()

def f(n):
    if n > 0:
        f(n // 4)
        sp.append(n)
        f(n - 1)

f(5)
print(sp)
print(''.join(list(map(str, sp))))