cnt = 0
for num in range(31):
    x = num
    while x > 0:
        if x // 5 == 0:
            if x == 3:
                cnt += 1
        x //= 5
print(cnt)