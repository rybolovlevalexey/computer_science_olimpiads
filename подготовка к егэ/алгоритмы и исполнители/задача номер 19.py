ans = set()
for num in range(128, 256):
    r = list(bin(num)[2:])
    r[3], r[4] = r[4], r[3]
    r[4], r[5] = r[5], r[4]
    r = int(''.join(r), 2)
    res = r - num
    ans.add(res)
print(len(ans))