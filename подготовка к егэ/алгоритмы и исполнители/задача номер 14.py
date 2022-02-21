def g(n):
    sp.append(n + 2)
    if n > 1:
        sp.append(n + 6)
        g(n - 1)
        g(n - 2)

sp = list()
g(19)
print(sum(sp))
for i in range(30):
    sp = list()
    g(i)
    res = (sum(sp))
    if res > 120000:
        print(i)
        break
