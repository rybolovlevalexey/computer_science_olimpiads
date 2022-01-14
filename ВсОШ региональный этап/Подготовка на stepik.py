number = int(input())
i1 = 0
i2 = 1
for i in range(number):
    i1, i2 = i2 % 10, (i1 + i2) % 10
print(i1)