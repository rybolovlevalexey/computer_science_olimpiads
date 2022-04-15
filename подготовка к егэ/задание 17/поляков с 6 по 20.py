sp = list()
for num in range(1305, 7850 + 1):
    if (num % 4 == 0 or num % 7 == 0) and num % 11 != 0 and num % 17 != 0 and num % 19 != 0 and num % 21 != 0:
        sp.append(num)
print(len(sp), min(sp))
