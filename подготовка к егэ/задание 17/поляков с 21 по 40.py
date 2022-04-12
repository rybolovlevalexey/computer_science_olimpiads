sp = list()
for num in range(1000, 9999 + 1):
    n = 0
    i = num
    while i > 0:
        i //= 3
        n += 1
    if num % 5 != 0 and num % 7 != 0 and num % 11 != 0 and n == 8:
        sp.append(num)
print(min(sp), max(sp))
