sp = list()
for num in range(1170, 8367 + 1):
    if (num % 3 == 0 or num % 7 == 0) and num % 11 != 0 and num % 13 != 0 and num % 17 != 0 and num % 19 != 0:
        sp.append(num)
print(len(sp), min(sp))
