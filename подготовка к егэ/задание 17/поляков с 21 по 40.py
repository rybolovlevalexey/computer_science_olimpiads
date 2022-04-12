sp = list()
for num in range(1000, 9999 + 1):
    n = 0
    i = num
    while i > 0:
        i //= 6
        n += 1
    if n <= 5 and (num % 6 == 4 or num % 6 == 3) and num // 6 % 6 == 1:
        sp.append(num)
print(len(sp), max(sp))
