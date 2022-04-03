ans = list()
def f(n):
    if n > 0:
        f(n - 4)
        ans.append(n)
        f(n // 3)
f(9)
print(sum(ans))
