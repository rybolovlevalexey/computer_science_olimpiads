num = 36**30 + 6**22 + 3 * 6**6 - 25
cnt = 0
print(num)
while num > 0:
    if num % 6 == 5:
        cnt += 1
    num //= 6
print(cnt)