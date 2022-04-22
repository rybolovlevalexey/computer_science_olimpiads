ans = list()
def f(n):
    if n > 0:
        ans.append(n)
        f(n - 3)
        f(n // 3)

f(9)
print(ans)
print(''.join(list(map(str, ans))))
