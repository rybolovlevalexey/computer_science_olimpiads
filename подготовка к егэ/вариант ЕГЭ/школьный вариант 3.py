num = 9**7 + 3**21 - 19
cnt = 0
while num > 0:
    if num % 3 == 2:
        cnt += 1
    num //= 3
print(cnt)