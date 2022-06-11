num = 8**2020 + 4**2017 + 26 - 1
cnt = 0
while num > 0:
    if num % 2 == 1:
        cnt += 1
    num //= 2
print(cnt)
num = 8**2020 + 4**2017 + 26 - 1
print(bin(num)[2:].count('1'))