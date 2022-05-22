num = 49**7 + 7**20 - 28
cnt = 0
while num > 0:
    if num % 7 == 6:
        cnt += 1
    num //= 7
print(cnt)