num = 4**511 + 2**511 - 511
num = bin(num)[2:]
print(num.count('1'))
num = 4**511 + 2**511 - 511
ans = 0
while num > 0:
    if num % 2 == 1:
        ans += 1
    num //= 2
print(ans)