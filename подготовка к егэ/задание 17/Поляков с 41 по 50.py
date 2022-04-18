sp = list()
for num in range(3721, 7752 + 1):
    if num % 3 == 0 and (num % 2 != 0 or (num // 2) % 2 != 0 or ((num // 2) // 2) % 2 != 0):
        sp.append(num)
print(len(sp), min(sp))
