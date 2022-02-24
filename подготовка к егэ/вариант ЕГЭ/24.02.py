num = 4**2020 + 2**2017 - 15
cnt = 0
while num > 0:
    if num % 2 == 1:
        cnt += 1
    num //= 2
print(cnt)