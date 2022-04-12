sp = list()
for num in range(1476, 7039 + 1):
    n = 0
    i = num
    while i > 0:
        i //= 4
        n += 1
    if num % 2 == 0 and num % 16 != 0 and num % 100 // 10 >= 4:
        sp.append(num)
print(len(sp), (max(sp) + min(sp)) // 2)
