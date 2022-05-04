ans = 0
for num in range(1, 100000):
    x = num
    a = b = 0
    while x > 0:
        a += 1
        b = b + (x % 100)
        x = x // 100
    if a == 2 and b == 15:
        ans = num
        print(num)
print(ans)