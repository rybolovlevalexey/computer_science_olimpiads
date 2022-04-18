sp = list()
n = 0
for num in range(-9563, -3102 - 1):
    x = abs(num)
    if x % 7 == 0 and x % 11 != 0 and x % 23 != 0 and x % 10 != 8:
        sp.append(num)
print(len(sp), max(sp))
