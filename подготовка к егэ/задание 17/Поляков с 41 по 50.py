sp = list()
for num in range(2371, 9432 + 1):
    if (num % 8 == 5 or num % 8 == 7) and num // 8 % 8 == 1 and num % 3 != 0 and num % 5 != 0:
        sp.append(num)
print(len(sp), max(sp))
