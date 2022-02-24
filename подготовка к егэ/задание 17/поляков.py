ans = []
for x in range(1012, 9638 + 1):
    if x % 3 == 0 and x % 11 != 0 and x % 13 != 0 and x % 17 != 0 and x % 19 != 0:
        ans.append(x)
print(len(ans), max(ans))
