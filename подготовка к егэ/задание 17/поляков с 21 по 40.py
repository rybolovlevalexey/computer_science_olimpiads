sp = list()
for num in range(1000, 9999 + 1):
    n = 0
    i = num
    while i > 0:
        i //= 5
        n += 1
    if n >= 6 and (num % 5 == 1 or num % 5 == 3) and num // 5 % 5 == 2:
        sp.append(num)
print(len(sp), min(sp))
