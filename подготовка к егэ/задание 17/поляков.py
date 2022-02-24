ans = list()
for x in range(117649, 823542 + 1):
    if x % 3 == 2 and x % 8 != 3 and x % 12 != 5:
        ans.append(x)
print(len(ans), max(ans))