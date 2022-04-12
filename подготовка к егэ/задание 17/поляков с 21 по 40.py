sp = list()
for num in range(1000, 9999 + 1):
    n = 0
    i = num
    while i > 0:
        i //= 4
        n += 1
    if num % 3 != 0 and num % 17 != 0 and num % 19 != 0 and n == 6:
        sp.append(num)
print(min(sp), max(sp))
