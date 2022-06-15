def f(n):
    sp.append(2*n + 1)
    if n > 1:
        sp.append(3*n - 8)
        f(n - 1)
        f(n - 4)


for num in range(10000):
    sp = list()
    f(num)
    res = sum(sp)
    if res > 5000000:
        print(num, res)
        break