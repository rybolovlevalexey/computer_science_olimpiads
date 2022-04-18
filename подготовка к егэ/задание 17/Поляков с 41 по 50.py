sp = list()
for num in range(3912, 9193 + 1):
    if sum(map(int, list(str(num)))) % 9 == 0 and (num % 16 != 1 or num // 16 % 16 != 2):
        sp.append(num)
print(len(sp), max(sp))
