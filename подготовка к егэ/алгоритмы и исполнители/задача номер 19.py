cnt = 0
for n in range(1, 10000):
    r = n
    if n % 6 == 0:
        r //= 3
    else:
        r -= 1
    if r % 5 == 0:
        r //= 5
    else:
        r -= 1
    if r % 3 == 0:
        r //= 3
    else:
        r -= 1
    if r == 4:
        print(n)
        cnt += 1
print(cnt)