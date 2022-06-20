num = 16**820 - 2**761 + 14
cnt = 0
while num > 0:
    if num % 4 == 0:
        cnt += 1
    num //= 4
print(cnt)