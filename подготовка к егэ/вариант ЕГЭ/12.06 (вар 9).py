cnt = 0
for num in range(100, 1000):
    n = num
    s1 = int(str(n)[0]) + int(str(n)[1])
    s2 = int(str(n)[1]) + int(str(n)[2])
    ans = ''.join(map(str, sorted([s1, s2])))
    if ans == '1216':
        cnt += 1
print(cnt)