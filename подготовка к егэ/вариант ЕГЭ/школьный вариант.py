cnt = 0
for num in range(100000):
    x = num
    a = b = 0
    while x > 0:
        a += 1
        b = b + (x % 100)
        x = x // 100
    if a == 2 and b == 12:
        cnt += 1
        print(num)
print(cnt)
