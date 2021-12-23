sp = list()
def F(n):
    if n > 0:
        F(n - 4)
        sp.append(n)
        F(n // 3)

F(9)
print(sum(sp))