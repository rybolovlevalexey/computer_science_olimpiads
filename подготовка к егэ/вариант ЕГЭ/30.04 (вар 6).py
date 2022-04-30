numbers = set()
start = 2

for i1 in [1, 2]:
    numbers.add(start + i1)
    for i2 in [1, 2]:
        numbers.add(start + i1 + i2)
        for i3 in [1, 2]:
            numbers.add(start + i1 + i2 + i3)
            for i4 in [1, 2]:
                numbers.add(start + i1 + i2 + i3 + i4)
print(numbers)
print(len(numbers))