sp = list()
def F(n):
    sp.append(2*n + 1)
    if n > 1:
        sp.append(3*n - 8)
        F(n - 1)
        F(n - 4)


for n in range(1, 100000):
    sp = list()
    F(n)
    if sum(sp) > 5000000:
        print(n, sum(sp))
        break