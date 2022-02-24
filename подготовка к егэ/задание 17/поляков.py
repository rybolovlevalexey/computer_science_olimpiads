ans = []
for x in range(1100, 11000 + 1):
    if x % 6 == 0 and x % 7 != 0 and x % 13 != 0 and x % 17 != 0 and x % 23 != 0:
        ans.append(x)
print(len(ans), max(ans))
