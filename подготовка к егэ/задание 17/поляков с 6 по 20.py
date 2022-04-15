sp = list()
for num in range(1056, 7563 + 1):
    if (num % 3 == 0 or num % 11 == 0) and num % 13 != 0 and num % 17 != 0 and num % 19 != 0 and num % 23 != 0:
        sp.append(num)
print(len(sp), min(sp))
