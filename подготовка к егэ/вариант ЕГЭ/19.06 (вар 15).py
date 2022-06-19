ans = list()
for num in range(1000, 10000):
    a, b, c, d = map(int, list(str(num)))
    s1 = a + b
    s2 = b + c
    s3 = c + d
    res = ''.join(list(map(str, sorted([s1, s2, s3])[1:])))
    if res == '1517':
        ans.append(num)
print(ans)
print(max(ans))