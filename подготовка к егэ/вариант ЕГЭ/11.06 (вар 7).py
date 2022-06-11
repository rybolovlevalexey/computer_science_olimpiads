cnt = 0
for num in range(1000, 10000):
    n = num
    a, b, c, d = map(int, list(str(num)))
    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0 or d % 2 == 0:
        continue
    s1 = a + b
    s2 = c + d
    st = ''.join(map(str, sorted([s1, s2])))
    if st == '414':
        cnt += 1
print(cnt)