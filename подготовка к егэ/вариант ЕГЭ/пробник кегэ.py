ans = list()
for num in range(1000000):
    s = num
    s = s // 100
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 128:
        ans.append(num)
print(ans)
print(max(ans))