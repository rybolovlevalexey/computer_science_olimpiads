num = (2**94 - 1) * (2**42 + 2)
cnt = 0
while num > 0:
    if num % 2 == 1:
        cnt += 1
    num //= 2
print(cnt)
num = (2**94 - 1) * (2**42 + 2)
print(str(bin(num)[2:]).count('1'))