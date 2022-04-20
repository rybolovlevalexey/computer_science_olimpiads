num = 16**25 - 2**32 - 32
cnt = 0
while num > 0:
    if num % 4 == 3:
        cnt += 1
    num //= 4
print(cnt)