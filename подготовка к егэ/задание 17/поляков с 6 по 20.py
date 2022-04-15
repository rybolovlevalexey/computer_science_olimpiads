sp = list()
for num in range(1045, 8963 + 1):
    if (num % 5 == 0 or num % 7 == 0) and num % 11 != 0 and num % 13 != 0 and num % 17 != 0 and num % 19 != 0:
        sp.append(num)
print(len(sp), min(sp))
