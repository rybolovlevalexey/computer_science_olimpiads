sp = list()
for num in range(2495, 7083 + 1):
    if (num % 16 == 10 or num % 16 == 15) and num // 16 % 16 == 1 and num % 5 != 0 and num % 9 != 0:
        sp.append(num)
print(len(sp), min(sp))
