n = int(input())
ans = 0
for i in range(1, n):
    x = int((n - i) / i**2)
    if x == 0:
        break
    ans += x
print(ans)