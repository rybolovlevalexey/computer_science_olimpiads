numbers = set()
for i1 in range(1, 7):
    for i2 in range(7):
        for i3 in range(7):
            for i4 in range(7):
                for i5 in range(7):
                    num = int(str(i1) + str(i2) + str(i3) + str(i4) + str(i5))
                    if len(set(str(num))) == 5 and (i1 % 2 != i2 % 2) and (i2 % 2 != i3 % 2) and (i3 % 2 != i4 % 2) and (i4 % 2 != i5 % 2):
                        numbers.add(num)
print(numbers)
print(len(numbers))