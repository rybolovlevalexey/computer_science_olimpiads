num = 3**75 + 27**17 + 9**6 - 17
cnt = 0
while num > 0:
    ost = num % 3
    num //= 3
    if ost == 2:
        cnt += 1
print(cnt)