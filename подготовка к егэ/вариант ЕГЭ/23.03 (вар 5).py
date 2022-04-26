num = 9**8 + 3**5 - 9
print(num)
cnt = 0
while num > 0:
    if num % 3 == 2:
        cnt += 1
    num //= 3
print(cnt)