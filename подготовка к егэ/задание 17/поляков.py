ans = []
for x in range(1512, 13202 + 1):
    if x % 7 == 0 and x % 11 != 0 and x % 13 != 0 and x % 17 != 0 and x % 23 != 0:
        ans.append(x)
print(len(ans), max(ans))
